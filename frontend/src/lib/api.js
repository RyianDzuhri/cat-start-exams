const BASE_URL = "/api";

// Peserta join exam
export async function joinExam(userId, token) {
  const res = await fetch(`${BASE_URL}/exam/join`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ user_id: userId, token })
  });
  if (!res.ok) throw new Error(`Error: ${res.status}`);
  return res.json();
}

// Pengawas generate token
export async function createSession(examId) {
  const res = await fetch(`${BASE_URL}/pengawas/create_session`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ exam_id: examId })
  });
  if (!res.ok) throw new Error(`Error: ${res.status}`);
  return res.json();
} 