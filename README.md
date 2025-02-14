# LinkedIn AI Agent 🤖

LinkedIn AI Job Application Agent, LinkedIn platformunda otomatik olarak yazılım geliştirici ilanlarına başvurmanıza yardımcı olan bir yapay zeka aracıdır. Bu proje, iş arayan geliştiricilerin LinkedIn'deki "Kolay Başvuru" (“Easy Apply”) iş ilanlarına otomatik olarak başvurmalarını sağlamak amacıyla geliştirilmiştir.

## Özellikler 🌟

- Otomatik LinkedIn Girişi: Kullanıcının e-posta ve şifresi ile otomatik LinkedIn oturumu açar.
- İş İlanlarını Tarama: "Software Developer" ilanlarını bulur ve iş ilanı detaylarını analiz eder.
- CV Uygunluk Analizi: İlan şartlarını PDF formatındaki CV ile karşılaştırarak uygun (✔️) veya uygunsuz (❌) olduğuna karar verir.
- Akıllı Başvuru Sistemi: İlgili iş ilanının başvuru formunu ilan detaylarına uygun şekilde doldurur.
- Tam Otomatik Başvuru: "Next" butonuna tıklayarak formu ilerletir ve "Submit Application" görünüyorsa başvuruyu tamamlar.
- Dış Bağlantı Kontrolü: Eğer başvuru harici bir siteye yönlendiriliyorsa, işlemi iptal eder ve bir sonraki ilana geçer.

## Gereksinimler 🛠️

- Python >=3.11
- PIP

## Kullanılan Teknolojiler

- PyPDF2
- Browser-use
- Playwright
- OpenAI

## Kurulum 🛠️

Projeyi yerel makinenizde çalıştırmak için aşağıdaki adımları izleyin:

1. **Depoyu Klonlayın**:
   ```bash
   git clone https://github.com/mesubasi/LinkedIn_AI_Agent.git
   cd LinkedIn_AI_Agent
   ```
2. **Gerekli Paketleri Yükleyin**:

   ```bash
   pip install browser-use
   playwright install
   ```

## Kullanım 💡

Program LinkedIn'e girip oturum açar.
Belirtilen kriterlere uygun iş ilanlarını arar.
CV'ye uygun ilanları işaretleyerek uygun olanlara otomatik başvurur.
"Easy Apply" sürecini tamamlar ve başvuruları gönderir.
Harici sitelere yönlendiren iş ilanlarını es geçer.
Başvurular tamamlandıktan sonra tarayıcıyı kapatmak için kullanıcı onay bekler.

## Notlar 📝

- Python 3.12.8 sürümü ile test edilmiştir
- Daha eski veya yeni sürümlerde sorunlar yaşanabilir
- Agent'in düzgün çalışabilmesi için .env dosyasını düzenlemeyi unutmayın
