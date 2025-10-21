const BASE_URL = "/api";

// Peserta bergabung ke ujian
export async function joinExam(userId, token) {
  const res = await fetch(`${BASE_URL}/exam/join`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ user_id: userId, token })
  });

  const data = await res.json(); // baca isi JSON dari Flask

  if (!res.ok) {
    // kalau Flask kirim error, lempar pesan dari server
    throw new Error(data.error || `HTTP ${res.status}`);
  }

  return data;
}

// Pengawas generate token
export async function createSession(examId) {
  const res = await fetch(`${BASE_URL}/pengawas/create_session`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ exam_id: examId })
  });

  const data = await res.json();

  if (!res.ok) {
    // kalau Flask kirim {"error": "..."} maka tampilkan isinya
    throw new Error(data.error || `HTTP ${res.status}`);
  }

  return data;
}
