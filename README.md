# noted

Dashboard belajar HSK dan catatan project pribadi.

## Learning Dashboard

Domain target: `learning.indraseptianto.my.id`

Materi:
- [HSK 1](https://drive.google.com/drive/folders/1tTeDRld3AzEjY9zySMCfgakOHvwwRJpf)
- [HSK 2](https://drive.google.com/drive/folders/1voKUefz1sBl4Z_u8ls2Fnx-0S-XwWFp1)
- [HSK 3](https://drive.google.com/drive/folders/1Pv9PomHhaHQMgUm3jc2OdkOVKL2w_yoV)

## Cronjob

Cronjob dibuat via GitHub Actions di `.github/workflows/daily-focus.yml`.

Jadwal:
- `0 0 * * *` UTC
- setara sekitar `07:00 WIB`

Action menjalankan:

```bash
python scripts/update_daily_focus.py
```

Output script:
- `data/daily.json`

Dashboard membaca `data/daily.json` untuk menampilkan fokus belajar harian.

## Deploy ke GitHub Pages

Recommended setting:
- Settings -> Pages
- Source: Deploy from a branch
- Branch: `main`
- Folder: `/ (root)`

Untuk domain custom:
- tambahkan `learning.indraseptianto.my.id` di Pages custom domain
- arahkan DNS CNAME `learning` ke `<username>.github.io`
