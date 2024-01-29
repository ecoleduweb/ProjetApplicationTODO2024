<!-- Page.svelte -->
<script lang="ts">
  // Import any dependencies you need
  import ToDo from "../Components/ToDo.svelte";
  // You can also define variables and functions here

  let pageTitle = "To Do"; // Example page title
  let taskToAdd: string = "";
  let taskList: string[] = [];
  let taskCompleted: string[] = [];

  function addTask() {
    if (taskToAdd.trim() !== "") {
      // Add a check to avoid adding empty tasks
      taskList = [...taskList, taskToAdd];
      taskToAdd = ""; // Clear the input field after adding the task
    }
  }

  function revertTask(index: number) {
    taskList = [...taskList, taskCompleted[index]];
    taskCompleted = taskCompleted.filter((task, i) => i !== index);
  }

  function deleteTask(index: number, completed = false) {
    if (completed) {
      taskCompleted = taskCompleted.filter((task, i) => i !== index);
    } else {
      taskList = taskList.filter((task, i) => i !== index);
    }
  }

  function updateTask(index: number) {
    taskCompleted = [...taskCompleted, taskList[index]];
    taskList = taskList.filter((task, i) => i !== index);
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
          <ToDo
            {task}
            {index}
            completed={false}
            {deleteTask}
            {updateTask}
            {revertTask}
          />
        {/each}
      </ul>
      <hr class="hor-line" />
    </div>
    <div class="task-completed">
      <h2>Tâche complété</h2>
      <ul class="list-group">
        {#each taskCompleted as task, index}
          <ToDo
            {task}
            {index}
            completed={true}
            {deleteTask}
            {updateTask}
            {revertTask}
          />
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
