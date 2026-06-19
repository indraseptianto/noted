# Notes - Crypto Forecast Watcher

## Ide Project

Project ini adalah sistem monitoring dan prediksi ringan untuk harga crypto menggunakan data time-series.

Tujuan awal bukan auto-trading, tapi membuat cronjob yang:
- mengambil data OHLCV crypto secara berkala,
- menyimpan data ke SQLite,
- menjalankan forecast/prediction,
- mendeteksi anomali harga, volume, dan volatilitas,
- mengirim alert atau daily report.

## VPS Target

Spesifikasi VPS:
- 2 CPU
- 8 GB RAM
- 80 GB disk total
- sekitar 40 GB disk kosong saat ide dibuat

Spek ini cukup untuk:
- data collector ringan,
- SQLite,
- cronjob forecast berkala,
- TimesFM inference ringan,
- alert/report.

Hindari:
- fine-tuning/training model besar di VPS,
- tick data resolusi sangat tinggi,
- terlalu banyak pair/timeframe di awal,
- menyimpan raw API response besar,
- log tanpa rotasi.

## Model

Model yang dipertimbangkan:
- Google Research TimesFM
- Repo: https://github.com/google-research/timesfm

TimesFM adalah model ML/foundation model untuk time-series forecasting.

Untuk crypto, TimesFM berperan sebagai mesin forecast, bukan aplikasi trading siap pakai.

Input:
- historical close price,
- OHLCV,
- volatility series,
- volume series.

Output:
- prediksi nilai masa depan,
- forecast harga/volume/volatility.

Layer tambahan tetap dibutuhkan:
- collector data,
- database,
- preprocessing,
- signal rules,
- alert/report,
- backtesting.

## Strategi Awal

Mulai sederhana:
- Pair: BTCUSDT, ETHUSDT, SOLUSDT
- Timeframe: 1h
- History: 90-365 hari
- Storage: SQLite
- Cron collector: tiap 1 jam
- Forecast job: tiap 4 jam atau harian
- Alert job: tiap 1 jam

Jangan mulai dengan:
- 100 pair,
- 1m candle,
- auto-trading,
- leverage signal,
- training berat.

## Fokus Prediction

Lebih realistis memprediksi:
- volatility,
- price range,
- anomaly,
- volume spike,
- trend probability,
- risk alert.

Kurang disarankan:
- prediksi harga pasti,
- sinyal BUY/SELL langsung,
- auto-trading tanpa backtest.

## Contoh Output Alert

```text
BTCUSDT 1H Forecast

Current: 67,200
Forecast 6H: 67,850
Forecast 24H: 68,100
Expected move 24H: +1.34%
Volatility forecast: naik
Volume anomaly: normal
Signal: bullish ringan, confidence rendah-sedang
```

```text
ETHUSDT Alert

Actual price 2.8% di bawah forecast band.
Volume 210% di atas normal.
Volatility spike terdeteksi.
Interpretasi: market anomaly, jangan entry tanpa konfirmasi.
```

## Arsitektur Rencana

```text
Crypto API
  -> data collector cron
  -> SQLite database
  -> preprocessing
  -> TimesFM / baseline forecast
  -> signal rules
  -> Telegram/Discord/email alert
  -> daily report
```

## Tahapan Implementasi

### Tahap 1 - Baseline Monitor

- Fetch OHLCV dari Binance/CoinGecko.
- Simpan ke SQLite.
- Hitung indikator ringan:
  - return,
  - moving average,
  - volatility,
  - volume z-score.
- Kirim alert rule-based.

### Tahap 2 - Forecast Baseline

- Tambahkan naive forecast.
- Tambahkan moving average / exponential smoothing.
- Simpan hasil forecast.
- Ukur error forecast.

### Tahap 3 - TimesFM

- Install TimesFM di environment terpisah.
- Jalankan inference berkala, bukan training.
- Bandingkan hasil TimesFM dengan baseline.
- Pakai hanya kalau performanya lebih baik atau insight-nya berguna.

### Tahap 4 - Reporting

- Buat daily report:
  - pair paling volatile,
  - anomaly terbesar,
  - forecast range,
  - trend summary,
  - risk notes.

## Cronjob Ide

- `crypto_collect_ohlcv`: tiap 1 jam
- `crypto_forecast`: tiap 4 jam atau harian
- `crypto_alert`: tiap 1 jam
- `crypto_daily_report`: tiap pagi/malam
- `vps_watchdog`: tiap 5-15 menit

## Disk/RAM Guard

Retention awal:
- OHLCV 1h: simpan 2 tahun
- OHLCV 15m: simpan 180 hari kalau dipakai
- Forecast result: simpan 90 hari
- Raw API response: jangan disimpan
- Logs: rotate 7 hari
- Backup DB: 7-14 hari

Alert resource:
- Disk > 80%
- RAM > 85%
- Load average tinggi
- DB terlalu besar
- Cronjob gagal
