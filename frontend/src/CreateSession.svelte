<script>
  import { createSession } from './lib/api.js';
  let examId = "";
  let token = "";
  let message = "";

  async function handleCreate() {
    if (!examId) {
      alert("Exam ID wajib diisi!");
      return;
    }
    try {
      const data = await createSession(examId);
      token = data.token;
      message = data.message;
    } catch (err) {
      alert(err.message);
    }
  }
</script>

<main>
  <h2>Create Exam Session (Pengawas)</h2>

  <label>
    Exam ID: 
    <input type="text" bind:value={examId} placeholder="Masukkan exam ID" />
  </label>
  <br/><br/>

  <button on:click={handleCreate}>Generate Token</button>

  {#if token}
    <div style="margin-top: 1rem; padding: 1rem; border: 1px solid #ccc;">
      <p><strong>Token:</strong> {token}</p>
      <p>{message}</p>
    </div>
  {/if}
</main>

<style>
  main { padding: 2rem; font-family: sans-serif; max-width: 400px; }
  input { width: 100%; padding: 0.5rem; margin-top: 0.3rem; }
  button { margin-top: 1rem; padding: 0.5rem 1rem; cursor: pointer; }
</style>
