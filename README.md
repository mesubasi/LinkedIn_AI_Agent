# LinkedIn AI Agent 🤖

LinkedIn AI Job Application Agent, LinkedIn platformunda otomatik olarak yazılım geliştirici ilanlarına başvurmanıza yardımcı olan bir yapay zeka aracıdır. Bu proje, iş arayan geliştiricilerin LinkedIn'deki "Kolay Başvuru" (“Easy Apply”) iş ilanlarına otomatik olarak başvurmalarını sağlamak amacıyla geliştirilmiştir.

## Özellikler 🌟

- Otomatik LinkedIn Girişi: Kullanıcının e-posta ve şifresi ile otomatik LinkedIn oturumu açar.
- İş İlanlarını Tarama: "Software Developer" ilanlarını bulur ve iş ilanı detaylarını analiz eder.
- CV Uygunluk Analizi: İlan şartlarını PDF formatındaki CV ile karşılaştırarak uygun (✔️) veya uygunsuz (❌) olduğuna karar verir.
- Akıllı Başvuru Sistemi: İlgili iş ilanının başvuru formunu ilan detaylarına uygun şekilde doldurur.
- Tam Otomatik Başvuru: "Next" butonuna tıklayarak formu ilerletir ve "Submit Application" görünüyorsa başvuruyu tamamlar.
- Dış Bağlantı Kontrolü: Eğer başvuru harici bir siteye yönlendiriliyorsa, işlemi iptal eder ve bir sonraki ilana geçer.

## Gereksinimler 🔧

- Python >=3.11
- PIP

## Kullanılan Teknolojiler 📚

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

3. **.env Dosyasını Oluşturun**:

   ```bash
   OPENAI_API_KEY=sk-fakeAPIKey1234567890xyz
   LINKEDIN_EMAIL=yourlinkedinmail@mail.com
   LINKEDIN_PASSWORD=password
   BROWSER_DRIVER_PATH=C:\Program Files\Google\Chrome\Application\chrome.exe
   CV_PATH=C:\Users\test\Desktop\cv.pdf
   ```

4. **Agent'i Çalıştırın**:

   ```bash
   python linkedin_ai_agent.py
   ```

## Kullanım 💡

1. Program LinkedIn'e girip oturum açar.
2. Belirtilen kriterlere uygun iş ilanlarını arar.
3. CV'ye uygun ilanları işaretleyerek uygun olanlara otomatik başvurur.
4. "Easy Apply" sürecini tamamlar ve başvuruları gönderir.
5. Harici sitelere yönlendiren iş ilanlarını es geçer.
6. Başvurular tamamlandıktan sonra tarayıcıyı kapatmak için kullanıcı onayı bekler.

## Notlar 📝

- Python 3.12.8 sürümü ile test edilmiştir
- Daha eski veya yeni sürümlerde sorunlar yaşanabilir
- Agent'in düzgün çalışabilmesi için .env dosyasını düzenlemeyi unutmayın
