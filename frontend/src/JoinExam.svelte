<script>
  import { joinExam } from './lib/api.js';

  let userId = "";
  let token = "";
  let examStarted = false;
  let questions = [];
  let message = "";
  let selectedAnswers = {};
  let timeLeft = 30 * 60; // 30 menit (dalam detik)
  let timer;

  async function handleJoin() {
    try {
      const data = await joinExam(userId, token);
      questions = data.questions;
      message = data.message;
      examStarted = true;
      startTimer();
    } catch (err) {
      alert(err.message);
    }
  }

  function startTimer() {
    clearInterval(timer);
    timer = setInterval(() => {
      if (timeLeft > 0) {
        timeLeft--;
      } else {
        clearInterval(timer);
        alert("Waktu habis!");
        examStarted = false;
      }
    }, 1000);
  }

  function formatTime(seconds) {
    const m = Math.floor(seconds / 60);
    const s = seconds % 60;
    return `${m.toString().padStart(2, "0")}:${s.toString().padStart(2, "0")}`;
  }

  function selectAnswer(qIndex, optionKey) {
    selectedAnswers[qIndex] = optionKey;
  }

  function handleSubmit() {
    console.log("Jawaban dipilih:", selectedAnswers);
    alert("Jawaban telah disimpan (simulasi)");
  }
</script>

<main>
  {#if !examStarted}
    <h2>Join Exam (Peserta)</h2>
    <label>User ID:</label>
    <input type="text" bind:value={userId} /><br />
    <label>Token:</label>
    <input type="text" bind:value={token} /><br />
    <button on:click={handleJoin}>Join Exam</button>
  {:else}
    <h2>Exam Started</h2>
    <p>{message}</p>
    <p><strong>Waktu tersisa:</strong> {formatTime(timeLeft)}</p>

    <ol>
      {#each questions as q, i}
        <li>
          <p>{q.text}</p>
          {#each Object.entries(q.options) as [key, val]}
            <label style="display: block; margin-bottom: 4px;">
              <input
                type="radio"
                name={"question-" + i}
                value={key}
                on:change={() => selectAnswer(i, key)}
                checked={selectedAnswers[i] === key}
              />
              {key.toUpperCase()}. {val}
            </label>
          {/each}
        </li>
      {/each}
    </ol>

    <button on:click={handleSubmit}>Submit Jawaban</button>
  {/if}
</main>

<style>
  main {
    padding: 2rem;
    font-family: sans-serif;
    max-width: 600px;
    margin: auto;
  }

  h2 {
    margin-bottom: 1rem;
  }

  label {
    display: block;
    margin-top: 0.5rem;
  }

  input[type="text"] {
    width: 100%;
    padding: 0.5rem;
    margin-bottom: 0.5rem;
  }

  button {
    margin-top: 1rem;
    padding: 0.5rem 1rem;
    cursor: pointer;
  }

  ol {
    margin-top: 1rem;
  }

  li {
    margin-bottom: 1rem;
  }
</style>
