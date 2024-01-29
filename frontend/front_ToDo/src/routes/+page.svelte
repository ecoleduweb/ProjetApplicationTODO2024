<!-- Page.svelte -->
<script>
  // Import any dependencies you need
  // You can also define variables and functions here

  let pageTitle = "To Do"; // Example page title
  let taskToAdd = "";
  let taskList = [];
  function addTask() {
    if (taskToAdd.trim() !== "") {
      // Add a check to avoid adding empty tasks
      taskList = [...taskList, taskToAdd];
      taskToAdd = ""; // Clear the input field after adding the task
    }
  }
</script>

<div class="page-container">
  <h1>{pageTitle}</h1>
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
  </form>
  <div class="task-added">
    <h2>Tâche à faire</h2>
    <ul>
      {#each taskList as task, index}
        <li class="list-task" key={index}>
          <input type="checkbox" name={`task${index}`} id={`task${index}`} />
          <label for={`task${index}`}>{task}</label>
          <button
            type="button"
            class="fa fa-trash input-delete"
            name={`toDelete${index}`}
            id="delete"
          >
          </button>
        </li>
      {/each}
    </ul>
    <hr class="hor-line" />
  </div>
  <div class="task-completed">
    <h2>Tâche complété</h2>
    <ul class="list-group">
      <!-- <li class="list-task">
        <input type="checkbox" name="task1" id="task1" />
        <label for="task1">Task 1</label>
        <button
          type="button"
          class="fa fa-trash input-delete"
          name="toDelete1"
          id="delete"
        >
        </button>
      </li> -->
    </ul>
  </div>
</div>

<style>
  h1,
  h2 {
    font-family: Manrope-ExtraLight;
  }
  p,
  li {
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
  .list-task {
    list-style-type: none;
  }
  .input-delete {
    margin: 0.52vw;
  }
  .hor-line {
    width: 100%;
  }
</style>
