<script>
  import StartExam from "./CreateSession.svelte";
  import JoinExam from "./JoinExam.svelte";

  let currentPage = ""; // "", "start", "join"
</script>

<main>
  {#if currentPage === ""}
    <h1>Exam Demo</h1>
    <button on:click={() => currentPage = "start"}>Start Exam</button>
    <button on:click={() => currentPage = "join"}>Join Exam</button>
  {/if}

  {#if currentPage === "start"}
    <StartExam />
    <button on:click={() => currentPage = ""}>Back</button>
  {/if}

  {#if currentPage === "join"}
    <JoinExam />
    <button on:click={() => currentPage = ""}>Back</button>
  {/if}
</main>

<style>
  main { padding: 2rem; font-family: sans-serif; }
  button { margin: 0.5rem; padding: 0.5rem 1rem; }
</style>
