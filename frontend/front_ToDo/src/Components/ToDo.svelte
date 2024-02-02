<!-- toDo.svelte -->
<script lang="ts">
  export let task;
  export let index;
  export let completed;
  export let deleteTask;
  export let updateTask;
</script>

<li class="list-task">
  <input
    type="checkbox"
    name={`task${task.id}`}
    id={`task${task.id}`}
    bind:checked={task.completed}
    on:click={() => updateTask(task.id)}
  />

  <label for={`task${task.id}`}>{task.task}</label>
  <button
    type="button"
    class="fa fa-trash input-delete"
    name={`toDelete${task.id}`}
    id="delete"
    on:click={() => deleteTask(task.id, completed)}
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
