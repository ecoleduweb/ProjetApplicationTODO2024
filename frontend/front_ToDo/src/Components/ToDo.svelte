<!-- toDo.svelte -->
<script lang="ts">
  export let task;
  export let index;
  export let completed;
  export let deleteTask;
  export let updateTask;
  export let revertTask;
</script>

<li class="list-task">
  <input
    type="checkbox"
    name={`task${index}`}
    id={`task${index}`}
    bind:checked={completed}
    on:click={() => (completed ? revertTask(index) : updateTask(index))}
  />

  <label for={`task${index}`}>{task}</label>
  <button
    type="button"
    class="fa fa-trash input-delete"
    name={`toDelete${index}`}
    id="delete"
    on:click={() => deleteTask(index, completed)}
  >
  </button>
</li>

<style>
  /* Add any additional styles here */
  .list-task {
    list-style-type: none;
  }
  .input-delete {
    margin: 0.52vw;
  }
  li {
    font-family: Manrope-Regular;
  }
</style>
