<script>
  import { joinExam } from './lib/api.js';
  let userId = "";
  let token = "";
  let examStarted = false;
  let questions = [];
  let message = "";

  async function handleJoin() {
    try {
      const data = await joinExam(userId, token);
      questions = data.questions;
      message = data.message;
      examStarted = true;
    } catch (err) {
      alert(err.message);
    }
  }
</script>

<main>
  {#if !examStarted}
    <h2>Join Exam (Peserta)</h2>
    <label>User ID: <input type="text" bind:value={userId} /></label><br/>
    <label>Token: <input type="text" bind:value={token} /></label><br/>
    <button on:click={handleJoin}>Join Exam</button>
  {:else}
    <h2>Exam Started</h2>
    <p>{message}</p>
    <ol>
      {#each questions as q}
        <li>
          <p>{q.text}</p>
          <ul>
            {#each Object.entries(q.options) as [key, val]}
              <li>{key}: {val}</li>
            {/each}
          </ul>
        </li>
      {/each}
    </ol>
  {/if}
</main>

<style>
  main { padding: 2rem; font-family: sans-serif; }
  input { margin-bottom: 0.5rem; }
</style>
