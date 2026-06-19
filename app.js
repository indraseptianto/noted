async function loadDailyFocus() {
  const fallback = {
    title: 'HSK 1 - 20 menit vocabulary',
    description: 'Kalau data cronjob belum ada, pakai fokus ringan: ulangi kosakata dasar, dengarkan audio, lalu tulis 5 contoh kalimat.',
    tasks: ['Review 10 kata', 'Dengar audio 10 menit', 'Tulis 5 kalimat pendek']
  };

  try {
    const response = await fetch('data/daily.json', { cache: 'no-store' });
    if (!response.ok) throw new Error(`daily.json ${response.status}`);
    renderDaily(await response.json());
  } catch (error) {
    renderDaily(fallback);
  }
}

function renderDaily(data) {
  document.querySelector('#daily-title').textContent = data.title;
  document.querySelector('#daily-desc').textContent = data.description;
  const list = document.querySelector('#daily-tasks');
  list.innerHTML = '';
  for (const task of data.tasks || []) {
    const item = document.createElement('li');
    item.textContent = task;
    list.appendChild(item);
  }
}

loadDailyFocus();
