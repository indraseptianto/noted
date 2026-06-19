#!/usr/bin/env python3
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data" / "daily.json"

PLAN = [
    {
        "level": "HSK 1",
        "title": "HSK 1 - Pinyin & sapaan",
        "description": "Bangun fondasi: pinyin, nada, sapaan, angka, dan kalimat pendek.",
        "tasks": ["Review 15 kosakata HSK 1", "Dengar audio 10 menit", "Tulis 5 kalimat sederhana"],
    },
    {
        "level": "HSK 1",
        "title": "HSK 1 - Listening pendek",
        "description": "Fokus telinga: dengarkan materi pendek dan ulangi dengan suara keras.",
        "tasks": ["Shadowing 10 menit", "Catat 5 kata sulit", "Baca ulang 1 dialog"],
    },
    {
        "level": "HSK 2",
        "title": "HSK 2 - Grammar ringan",
        "description": "Naik level dengan pola kalimat harian, tempat, waktu, dan aktivitas.",
        "tasks": ["Review 1 pola grammar", "Buat 8 contoh kalimat", "Ulangi 20 kosakata HSK 2"],
    },
    {
        "level": "HSK 2",
        "title": "HSK 2 - Reading drill",
        "description": "Latihan membaca cepat dan memahami konteks kalimat sederhana.",
        "tasks": ["Baca 1 teks pendek", "Tandai kata baru", "Ringkas isi teks dalam Bahasa Indonesia"],
    },
    {
        "level": "HSK 3",
        "title": "HSK 3 - Connector & konteks",
        "description": "Fokus memahami kalimat lebih panjang dan hubungan antaride.",
        "tasks": ["Review connector", "Baca 1 paragraf", "Tulis 3 kalimat kompleks"],
    },
    {
        "level": "HSK 3",
        "title": "HSK 3 - Mixed listening",
        "description": "Latihan listening lebih natural dengan target menangkap ide utama.",
        "tasks": ["Dengar audio 15 menit", "Catat keyword", "Ulangi 5 kalimat yang terdengar"],
    },
    {
        "level": "Review",
        "title": "Weekly review - HSK 1 sampai 3",
        "description": "Hari checkpoint: rapikan catatan, ulangi bagian lemah, dan pilih fokus minggu depan.",
        "tasks": ["Review semua catatan minggu ini", "Pilih 10 kata tersulit", "Tentukan target minggu depan"],
    },
]


def main() -> None:
    today = datetime.now(timezone.utc).date()
    item = PLAN[today.toordinal() % len(PLAN)]
    payload = {
        **item,
        "date": today.isoformat(),
        "updated_at": datetime.now(timezone.utc).isoformat(),
        "materials": {
            "hsk1": "https://drive.google.com/drive/folders/1tTeDRld3AzEjY9zySMCfgakOHvwwRJpf",
            "hsk2": "https://drive.google.com/drive/folders/1voKUefz1sBl4Z_u8ls2Fnx-0S-XwWFp1",
            "hsk3": "https://drive.google.com/drive/folders/1Pv9PomHhaHQMgUm3jc2OdkOVKL2w_yoV",
        },
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Updated {OUT.relative_to(ROOT)}: {payload['title']}")


if __name__ == "__main__":
    main()
