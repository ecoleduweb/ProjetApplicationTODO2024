<!-- Page.svelte -->
<script lang="ts">
  // Import any dependencies you need
  import ToDo from "../Components/ToDo.svelte";
  // You can also define variables and functions here
  import { onMount } from "svelte";

  let pageTitle = "To Do"; // Example page title
  let taskToAdd: string = "";
  let id = 0;
  let taskList = [];
  let taskCompleted = [];

  onMount(async () => {
    const res = await fetch("http://localhost:3001/getAllTodos");
    const data = await res.json();
    for (let i = 0; i < data.todos.length; i++) {
      if (data.todos[i].completed) {
        taskCompleted = [...taskCompleted, data.todos[i]];
      } else {
        taskList = [...taskList, data.todos[i]];
        console.log(data.todos[i].task);
      }
    }
  });
  async function addTask() {
    if (taskToAdd.trim() !== "") {
      // Add a check to avoid adding empty tasks
      const res = await fetch("http://localhost:3001/addTodo", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ task: taskToAdd, completed: false }),
      });
      const data = await res.json();
      console.log(data);
      taskList = [
        ...taskList,
        { task: taskToAdd, id: data.todo.id, completed: false },
      ];
      id++;
      taskToAdd = ""; // Clear the input field after adding the task
      console.log(taskList);
    }
  }

  async function deleteTask(index: number, completed = false) {
    if (completed) {
      taskCompleted = taskCompleted.filter((task, i) => i !== index);
    } else {
      taskList = taskList.filter((task, i) => i !== index);
    }
    const res = await fetch("http://localhost:3001/deleteTodo/" + index, {
      method: "DELETE",
      headers: {
        "Content-Type": "application/json",
      },
    });
    const data = await res.json();
    console.log(data);
  }

  async function updateTask(taskId) {
    const index = taskList.findIndex((task) => task.id === taskId);
    console.log(taskId);

    if (index !== -1) {
      const updatedTask = taskList[index];
      taskList = taskList.filter((task) => task.id !== taskId);
      updatedTask.completed = !updatedTask.completed;
      taskCompleted = [...taskCompleted, updatedTask];
      const res = await fetch("http://localhost:3001/updateTodo/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          completed: updatedTask.completed,
          id: taskId,
          task: updatedTask.task,
        }),
      });
      const data = await res.json();
      console.log(data);
    } else {
      const completedIndex = taskCompleted.findIndex(
        (task) => task.id === taskId
      );

      if (completedIndex !== -1) {
        const updatedCompletedTask = taskCompleted[completedIndex];
        taskCompleted = taskCompleted.filter((task) => task.id !== taskId);
        updatedCompletedTask.completed = !updatedCompletedTask.completed;
        taskList = [...taskList, updatedCompletedTask];

        onMount(async () => {
          const res = await fetch("http://localhost:3001/updateTodo/", {
            method: "PUT",
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify({
              completed: updatedCompletedTask.completed,
              id: taskId,
              task: updatedCompletedTask.task,
            }),
          });
          const data = await res.json();
          console.log(data);
        });
      }
    }
  }
</script>

<div class="page-container">
  <h1>{pageTitle}</h1>
  <!-- Your existing HTML... -->
  <p>Page des ToDo en Svelte</p>
  <form action="">
    <div class="column-add">
      <p class="input-label">Ajouter une tâche</p>
      <input
        type="text"
        class="input-text"
        name="task"
        id="task"
        bind:value={taskToAdd}
      />
      <input
        type="button"
        class="input-button"
        name="addTask"
        id="toAdd"
        value="Ajouter"
        on:click={addTask}
      />
      <hr class="hor-line" />
    </div>
    <div class="task-added">
      <h2>Tâche à faire</h2>
      <ul>
        {#each taskList as task, index}
          <ToDo {task} {index} completed={false} {deleteTask} {updateTask} />
        {/each}
      </ul>
      <hr class="hor-line" />
    </div>
    <div class="task-completed">
      <h2>Tâche complété</h2>
      <ul class="list-group">
        {#each taskCompleted as task, index}
          <ToDo {task} {index} completed={true} {deleteTask} {updateTask} />
        {/each}
      </ul>
    </div>
  </form>
</div>

<style>
  h1,
  h2 {
    font-family: Manrope-ExtraLight;
  }
  p {
    font-family: Manrope-Regular;
  }
  /* Add your CSS styles here */
  .page-container {
    padding: 20px;
    background-color: #ececec;
    display: flex;
    flex-direction: column;
    width: 100%;
    height: 100vh;
  }

  h1 {
    color: #333;
  }
  .column-add {
    width: 15%;
    flex-direction: column;
    display: flex;
  }
  .task-added {
    width: 15%;
    flex-direction: column;
    display: flex;
  }
  .input-button,
  .input-text,
  .input-label {
    padding: 0%;
    margin: 0%;
    box-sizing: border-box;
    margin: 0.26vw;
  }
  .input-text {
    width: 70%;
  }
  .input-button {
    width: 30%;
  }
  .hor-line {
    width: 100%;
  }
</style>
