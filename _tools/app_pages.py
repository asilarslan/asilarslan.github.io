#!/usr/bin/env python3
"""Civics Prep ve LiD Trainer sayfalarını üretir: python3 _tools/app_pages.py
Uygulama repoları (~/us-citizenship, ~/leben-in-deutschland) gerekli; simge ve ekranlar oradan alınır."""
import os, shutil, subprocess, sys

SITE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # repo kökü
MAIL = "support@asilarslan.com"
UPDATED = {"en": "Effective November 8, 2026", "es": "Vigente desde el 8 de noviembre de 2026",
           "de": "Stand: 8. November 2026", "tr": "Yürürlük tarihi: 8 Kasım 2026", "ar": "سارية اعتبارًا من 8 نوفمبر 2026"}

CSS = """*{box-sizing:border-box}body{margin:0;background:%(bg)s;color:#e3e9f2;font:17px/1.65 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif}
a{color:%(accent)s}main{max-width:820px;margin:0 auto;padding:28px 20px 60px}
.nav{display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:10px;max-width:820px;margin:0 auto;padding:18px 20px;border-bottom:1px solid %(line)s}
.brand{display:flex;align-items:center;gap:10px;color:#fff;text-decoration:none;font-weight:800}
.brand img{width:34px;height:34px;border-radius:8px}.navlinks a{margin-left:16px;font-size:14px;color:#9aa7ba;text-decoration:none}
.navlinks a:hover{color:%(accent)s}h1{font-size:30px;margin:18px 0 4px}
h2{font-size:18px;color:%(accent)s;margin-top:30px}.lead{font-size:19px}.muted{color:#9aa7ba;font-size:14px}
.shots{display:flex;gap:12px;overflow-x:auto;padding:8px 0 4px;margin:18px 0}.shots img{height:420px;border-radius:12px;flex:none}
.note{border-left:3px solid %(accent)s;padding:4px 14px;color:#c4cedb}hr{border:0;border-top:1px solid %(line)s;margin:36px 0}
[dir=rtl] h2,[dir=rtl] p,[dir=rtl] li{text-align:right}
footer{max-width:820px;margin:0 auto;padding:0 20px 40px;color:#76839a;font-size:13px}
@media(max-width:520px){.shots img{height:340px}.navlinks a{margin-left:10px}}
"""

def page(app, slug, title, body, lang, depth):
    up = "../" if depth else ""
    nav = app["nav"]
    return f"""<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><meta name="description" content="{app['desc']}">
<link rel="icon" href="{up}assets/icon.png"><link rel="stylesheet" href="{up}assets/styles.css"></head><body>
<nav class="nav"><a class="brand" href="{up or './'}"><img src="{up}assets/icon.png" alt=""> {app['name']}</a>
<div class="navlinks"><a href="{up}support/">{nav[0]}</a><a href="{up}privacy-policy/">{nav[1]}</a><a href="{up}terms-of-use/">{nav[2]}</a></div></nav>
<main>
{body}
</main><footer>© 2026 Asil Arslan · <a href="mailto:{MAIL}">{MAIL}</a> · {app['footer']}</footer></body></html>
"""

def mail(subject):
    return f'<a href="mailto:{MAIL}?subject={subject.replace(" ", "%20")}">{MAIL}</a>'

# ---------------------------------------------------------------- Civics Prep
civics = dict(
    slug="civics-prep", name="Civics Prep", repo="~/us-citizenship", icon="ios/CivicsPrep/Resources/Assets.xcassets/AppIcon.appiconset/icon-1024.png",
    shots=("docs/store/app-store/iphone-6.9-1320x2868/en", ["01-01-today", "02-04-interview", "03-02-card", "04-03-quiz", "05-06-map", "06-05-interview-history"]),
    css=dict(bg="#101a2e", accent="#8fc0f5", line="#22324d"),
    desc="Civics Prep: practice for the 2025 U.S. citizenship civics test on iPhone, iPad and Android.",
    nav=("Support", "Privacy", "Terms"), footer="Not affiliated with USCIS",
)
civics["index"] = f"""<h1>Civics Prep</h1><p class="muted">U.S. Citizenship Test 2025 · Examen de ciudadanía 2025 · English / Español</p>
<div class="shots">{{shots}}</div>
<p class="note">Civics Prep is an independent study app. It is not affiliated with U.S. Citizenship and Immigration Services (USCIS) or any government agency. Questions come from the public USCIS study materials at <a href="https://www.uscis.gov/citizenship/find-study-materials-and-resources/study-for-the-test">uscis.gov</a>.</p>
<p class="lead">Practice all 128 questions of the 2025 civics test, then take a practice interview that follows the real rules: questions are read aloud, 12 correct answers pass and 9 wrong answers end the interview.</p>
<ul><li>Flashcards with spaced review and 10-question quizzes</li><li>Answers for your state, senators, representative and governor</li><li>Interactive map of the states and capitals</li><li>Reading and writing vocabulary for the English test</li><li>Every question in Spanish as an unofficial study aid</li><li>Works offline, no account; your progress stays on your device</li></ul>
<p>Free with ads. Civics Prep Pro is a one-time purchase that removes ads and unlocks unlimited practice interviews and the map game.</p>
<hr><p class="lead">Practique las 128 preguntas del examen de educación cívica 2025 y haga una entrevista de práctica con las reglas reales. Todas las preguntas tienen traducción al español como ayuda de estudio no oficial; la entrevista real es en inglés.</p>
<p>Civics Prep es una aplicación independiente y no está afiliada a USCIS ni a ninguna agencia del gobierno.</p>
<p><a href="support/">Support · Soporte</a> · <a href="privacy-policy/">Privacy · Privacidad</a> · <a href="terms-of-use/">Terms · Términos</a></p>"""

civics["support"] = f"""<h1>Support</h1>
<p class="lead">Questions or found a mistake? Email {mail('Civics Prep Support')} with your device model and OS version.</p>
<h2>Which test does the app cover?</h2><p>The 2025 civics test with 128 questions. If you filed Form N-400 before October 20, 2025, you take the 2008 test with 100 questions; check the date on your notice and the <a href="https://www.uscis.gov/citizenship/find-study-materials-and-resources/study-for-the-test">USCIS study page</a>.</p>
<h2>How does the practice interview work?</h2><p>The officer asks up to 20 questions. You pass with 12 correct answers; the interview stops after 9 wrong answers. If you are 65 or older with 20 years of permanent residence, turn on 65/20 special consideration under More: 10 questions from the starred list, 6 correct to pass.</p>
<h2>Why do some answers mention my state?</h2><p>Some answers depend on where you live. Pick your state under More and add your senators, representative and governor. Elected officials change; check <a href="https://www.uscis.gov/citizenship/testupdates">uscis.gov/citizenship/testupdates</a> before your interview.</p>
<h2>I found a wrong answer</h2><p>Please email us the question number. We follow the official USCIS list and fix errors in the next update.</p>
<h2>Restore my Pro purchase</h2><p>Open Pro and tap Restore purchase, signed in with the same Apple ID or Google account you bought it with.</p>
<h2>Where is my progress saved?</h2><p>On your device only, and in your device backup. Deleting the app deletes your progress.</p>
<hr><h1>Soporte</h1>
<p class="lead">¿Preguntas o encontró un error? Escriba a {mail('Civics Prep Soporte')} con el modelo de su dispositivo y la versión del sistema.</p>
<h2>¿Qué examen cubre la app?</h2><p>El examen de educación cívica 2025 con 128 preguntas. Si presentó el formulario N-400 antes del 20 de octubre de 2025, le corresponde el examen de 2008 con 100 preguntas.</p>
<h2>¿Cómo funciona la entrevista de práctica?</h2><p>Hasta 20 preguntas; aprueba con 12 correctas y termina con 9 incorrectas. Con la opción 65/20: 10 preguntas de la lista marcada, 6 correctas para aprobar.</p>
<h2>Restaurar mi compra Pro</h2><p>Abra Pro y toque Restaurar compra con la misma cuenta de Apple o Google.</p>
<h2>¿Dónde se guarda mi progreso?</h2><p>Solo en su dispositivo y en su copia de seguridad. Si borra la app, se borra su progreso.</p>"""

civics["privacy"] = f"""<h1>Privacy Policy</h1><p class="muted">{UPDATED['en']} · Español abajo</p>
<p>This policy covers the Civics Prep app for iPhone, iPad and Android, published by Asil Arslan. Civics Prep is not affiliated with USCIS or any government agency.</p>
<h2>No accounts, no servers</h2><p>The app has no sign-in and we run no servers for it. Your progress, settings, practice interview results and the names you enter (such as your senators) are stored only on your device and in your device backup. We cannot see them.</p>
<h2>Ads</h2><p>The free version shows ads from Google AdMob after a quiz, review or practice interview, and an optional rewarded ad for an extra interview. To show and measure ads, AdMob may collect your device's advertising identifier, IP address, approximate location derived from it, and ad interaction data. On iOS, the app asks for permission before tracking; if you say no, ads are not personalized. Where required (for example in the EEA and the UK), Google's consent form asks for your choice, and you can change it any time under More › Ad privacy choices. See <a href="https://policies.google.com/technologies/partner-sites">how Google uses information from apps that use its services</a>. Pro users see no ads, and the ad SDK is not used to show them ads.</p>
<h2>Purchases</h2><p>Pro is sold through the App Store or Google Play. We do not receive your payment details; we only learn from the store whether Pro is active on your device.</p>
<h2>Speech</h2><p>Questions are read aloud by your device's built-in text-to-speech. The app does not record or upload your voice.</p>
<h2>Links</h2><p>Links to uscis.gov, senate.gov and house.gov open in your browser; those sites have their own privacy policies.</p>
<h2>Children</h2><p>The app is meant for adults preparing for the naturalization interview and is not directed at children under 13.</p>
<h2>Deleting your data</h2><p>Use More › Reset my progress, or delete the app. Because we hold no data about you, there is nothing to delete on our side.</p>
<h2>Changes and contact</h2><p>We will post changes on this page. Questions: <a href="mailto:{MAIL}">{MAIL}</a></p>
<hr><h1>Política de privacidad</h1><p class="muted">{UPDATED['es']}</p>
<p>Esta política cubre la app Civics Prep para iPhone, iPad y Android, publicada por Asil Arslan. Civics Prep no está afiliada a USCIS ni a ninguna agencia del gobierno.</p>
<h2>Sin cuentas ni servidores</h2><p>La app no tiene inicio de sesión y no usamos servidores. Su progreso, ajustes, resultados y los nombres que escribe (como sus senadores) se guardan solo en su dispositivo y en su copia de seguridad. No podemos verlos.</p>
<h2>Anuncios</h2><p>La versión gratuita muestra anuncios de Google AdMob al terminar una prueba, un repaso o una entrevista, y un anuncio opcional con recompensa para una entrevista adicional. AdMob puede recopilar el identificador de publicidad, la dirección IP, la ubicación aproximada derivada de ella y datos de interacción con anuncios. En iOS, la app pide permiso antes de rastrear; si dice que no, los anuncios no se personalizan. Donde es obligatorio, el formulario de consentimiento de Google le permite elegir, y puede cambiar su elección en Más › Opciones de privacidad de anuncios. Consulte <a href="https://policies.google.com/technologies/partner-sites?hl=es">cómo usa Google la información</a>. Los usuarios Pro no ven anuncios.</p>
<h2>Compras</h2><p>Pro se vende a través de App Store o Google Play. No recibimos sus datos de pago.</p>
<h2>Voz</h2><p>Las preguntas se leen con la voz integrada del dispositivo. La app no graba ni envía su voz.</p>
<h2>Niños</h2><p>La app está pensada para adultos y no está dirigida a menores de 13 años.</p>
<h2>Borrar sus datos</h2><p>Use Más › Borrar mi progreso o borre la app. No guardamos datos suyos.</p>
<h2>Contacto</h2><p><a href="mailto:{MAIL}">{MAIL}</a></p>"""

civics["terms"] = f"""<h1>Terms of Use</h1><p class="muted">{UPDATED['en']} · Español abajo</p>
<p>Civics Prep is licensed to you for personal, non-commercial use through the store you obtained it from, under that store's standard terms (for the App Store, Apple's <a href="https://www.apple.com/legal/internet-services/itunes/dev/stdeula/">Standard Licensed Application End User License Agreement</a>).</p>
<h2>Not legal advice, not official</h2><p>Civics Prep is a study aid. It is not affiliated with USCIS, does not give legal or immigration advice and does not guarantee that you will pass. The questions and answers follow the public USCIS study materials; the official materials and your USCIS notices always take precedence. Spanish translations are unofficial.</p>
<h2>Pro</h2><p>Civics Prep Pro is a one-time in-app purchase, not a subscription. Refunds are handled by Apple or Google under their policies.</p>
<h2>The app</h2><p>The app is provided as is. We work to keep the content correct and current but cannot guarantee it is free of errors. Your progress is stored only on your device; we cannot restore it if it is lost.</p>
<h2>Ownership</h2><p>The app's code and design belong to Asil Arslan. Question texts are U.S. government works from USCIS. Map outlines are based on public-domain U.S. Census Bureau data.</p>
<h2>Contact</h2><p><a href="mailto:{MAIL}">{MAIL}</a></p>
<hr><h1>Términos de uso</h1><p class="muted">{UPDATED['es']}</p>
<p>Civics Prep se le concede bajo licencia para uso personal y no comercial a través de la tienda donde la obtuvo y según sus términos estándar.</p>
<h2>No es asesoría legal ni oficial</h2><p>Civics Prep es una ayuda de estudio. No está afiliada a USCIS, no ofrece asesoría legal ni migratoria y no garantiza que apruebe. Los materiales oficiales de USCIS siempre tienen prioridad. Las traducciones al español no son oficiales.</p>
<h2>Pro</h2><p>Civics Prep Pro es una compra única, no una suscripción. Los reembolsos los gestionan Apple o Google.</p>
<h2>Contacto</h2><p><a href="mailto:{MAIL}">{MAIL}</a></p>"""
civics["titles"] = ("Civics Prep", "Civics Prep Support", "Civics Prep Privacy Policy", "Civics Prep Terms of Use")
civics["lang"] = "en"

# ---------------------------------------------------------------- LiD Trainer
lid = dict(
    slug="lid-trainer", name="LiD Trainer", repo="~/leben-in-deutschland", icon="ios/LidTrainer/Resources/Assets.xcassets/AppIcon.appiconset/icon-1024.png",
    shots=("docs/store/app-store/iphone-6.9-1320x2868/de", ["01-01-today", "02-04-exam", "03-02-practice", "04-03-image", "05-05-exam-history", "06-06-study"]),
    css=dict(bg="#0f1d1a", accent="#7fdcc6", line="#203a34"),
    desc="LiD Trainer: Lern-App für den Einbürgerungstest und „Leben in Deutschland“, auf Deutsch, Türkisch und Arabisch.",
    nav=("Support", "Datenschutz", "Nutzungsbedingungen"), footer="Keine Behörden-App",
)
lid["index"] = f"""<h1>LiD Trainer</h1><p class="muted">Einbürgerungstest &amp; Leben in Deutschland · Deutsch / Türkçe / العربية</p>
<div class="shots">{{shots}}</div>
<p class="note">LiD Trainer ist eine unabhängige Lern-App. Sie wird nicht vom Bundesamt für Migration und Flüchtlinge (BAMF) oder einer anderen Behörde herausgegeben. Die Fragen stammen aus dem öffentlich veröffentlichten <a href="https://www.bamf.de/SharedDocs/Anlagen/DE/Integration/Einbuergerung/gesamtfragenkatalog-lebenindeutschland.html">Gesamtfragenkatalog</a>.</p>
<p class="lead">Alle 460 Fragen (Stand 07.05.2025) mit allen Bildfragen, eine Testsimulation mit 33 Fragen in 60 Minuten und auf Wunsch eine Übersetzung ins Türkische und Arabische.</p>
<ul><li>Tägliche Wiederholung: falsch beantwortete Fragen kommen öfter</li><li>Lernen nach Themen und für dein Bundesland</li><li>Fehlertraining und Vorlesefunktion</li><li>Offline, ohne Konto; dein Fortschritt bleibt auf deinem Gerät</li></ul>
<p>Kostenlos mit Werbung. LiD Trainer Pro ist ein Einmalkauf ohne Abo: unbegrenzte Testsimulationen und keine Werbung.</p>
<hr><p class="lead">460 sorunun tamamı, 60 dakikalık 33 soruluk sınav provası ve her sorunun altında isteğe bağlı Türkçe çeviri. Sınavın kendisi Almancadır; çeviriler resmî değildir.</p>
<p>LiD Trainer bağımsız bir uygulamadır; BAMF ya da başka bir kurumla bağlantısı yoktur.</p>
<hr><div dir="rtl" lang="ar"><p class="lead">جميع الأسئلة الـ 460، واختبار تجريبي من 33 سؤالًا في 60 دقيقة، وترجمة عربية اختيارية تحت كل سؤال. الاختبار نفسه باللغة الألمانية، والترجمات غير رسمية.</p>
<p>LiD Trainer تطبيق مستقل، ولا يصدر عن المكتب الاتحادي للهجرة واللاجئين (BAMF) أو أي جهة رسمية.</p></div>
<p><a href="support/">Support · Destek · الدعم</a> · <a href="privacy-policy/">Datenschutz · Gizlilik · الخصوصية</a> · <a href="terms-of-use/">Nutzungsbedingungen · Koşullar · الشروط</a></p>"""

lid["support"] = f"""<h1>Support</h1>
<p class="lead">Fragen oder einen Fehler gefunden? Schreib an {mail('LiD Trainer Support')} mit Gerätemodell und Systemversion.</p>
<h2>Wie läuft der Test ab?</h2><p>33 Fragen: 30 allgemeine und 3 zu deinem Bundesland, 60 Minuten. Für den Einbürgerungstest brauchst du 17 richtige Antworten, für das Zertifikat „Leben in Deutschland“ 15. Du kannst Antworten bis zur Abgabe ändern.</p>
<h2>Mein Bundesland ändern</h2><p>Mehr › Einstellungen › Bundesland. Die Testsimulation nimmt dann die Fragen dieses Landes.</p>
<h2>Ich habe eine falsche Antwort gefunden</h2><p>Der amtliche Katalog markiert die richtigen Antworten nicht; wir haben sie für die App ermittelt und geprüft. Schick uns bitte die Fragennummer, wir korrigieren sie im nächsten Update.</p>
<h2>Pro wiederherstellen</h2><p>Öffne Pro und tippe auf „Kauf wiederherstellen“, mit derselben Apple-ID bzw. demselben Google-Konto.</p>
<h2>Wo wird mein Fortschritt gespeichert?</h2><p>Nur auf deinem Gerät und in dessen Backup. Wenn du die App löschst, ist der Fortschritt weg.</p>
<hr><h1>Destek</h1>
<p class="lead">Sorun mu var, hata mı buldun? Cihaz modelini ve sistem sürümünü yazarak {mail('LiD Trainer Destek')} adresine yaz.</p>
<h2>Sınav nasıl?</h2><p>33 soru: 30 genel ve 3 eyalet sorusu, 60 dakika. Vatandaşlık testi için 17, „Leben in Deutschland“ sertifikası için 15 doğru gerekir.</p>
<h2>Çeviriler</h2><p>Arayüz dili Türkçe olduğunda soruların altında isteğe bağlı Türkçe çeviri görünür. Sınavda sorular Almancadır; çeviriler resmî değildir.</p>
<h2>Pro'yu geri yükleme</h2><p>Pro ekranında „Satın alımı geri yükle“ye dokun; aynı Apple ya da Google hesabıyla.</p>
<hr><div dir="rtl" lang="ar"><h1>الدعم</h1>
<p class="lead">هل لديك سؤال أو وجدت خطأ؟ راسلنا على {mail('LiD Trainer Support AR')} مع طراز الجهاز وإصدار النظام.</p>
<h2>كيف يجري الاختبار؟</h2><p>33 سؤالًا: 30 سؤالًا عامًا و3 أسئلة عن ولايتك، خلال 60 دقيقة. تحتاج إلى 17 إجابة صحيحة لاختبار التجنيس و15 لشهادة „Leben in Deutschland“.</p>
<h2>استعادة Pro</h2><p>افتح Pro واضغط „استعادة الشراء“ بنفس حساب Apple أو Google.</p></div>"""

lid["privacy"] = f"""<h1>Datenschutzerklärung</h1><p class="muted">{UPDATED['de']} · Türkçe ve العربية aşağıda</p>
<p>Diese Erklärung gilt für die App LiD Trainer für iPhone, iPad und Android. LiD Trainer wird nicht vom BAMF oder einer anderen Behörde herausgegeben.</p>
<h2>Verantwortlicher</h2><p>Asil Arslan, E-Mail: <a href="mailto:{MAIL}">{MAIL}</a></p>
<h2>Keine Konten, keine Server</h2><p>Die App hat keine Anmeldung, und wir betreiben keine Server für sie. Lernfortschritt, Einstellungen und Testergebnisse werden nur auf deinem Gerät und in dessen Backup gespeichert. Wir haben darauf keinen Zugriff.</p>
<h2>Werbung (Google AdMob)</h2><p>In der kostenlosen Version zeigt Google AdMob (Google Ireland Limited, Gordon House, Barrow Street, Dublin 4, Irland) nach einer Übung oder Testsimulation Werbung sowie auf Wunsch ein Werbevideo für eine zusätzliche Testsimulation. Dabei können die Werbe-ID deines Geräts, die IP-Adresse, ein daraus abgeleiteter ungefährer Standort und Interaktionen mit Anzeigen verarbeitet werden, auch in Ländern außerhalb der EU. Beim ersten Start fragt Googles Einwilligungsformular, ob du personalisierte Werbung erlaubst (Art. 6 Abs. 1 lit. a DSGVO, § 25 Abs. 1 TDDDG). Ohne Einwilligung wird nur nicht personalisierte Werbung gezeigt. Du kannst deine Wahl jederzeit unter Mehr › Datenschutzoptionen für Werbung ändern oder widerrufen. Unter iOS fragt die App außerdem vor dem Tracking nach deiner Erlaubnis. Mehr dazu: <a href="https://policies.google.com/technologies/partner-sites?hl=de">Nutzung von Daten durch Google</a>. Mit Pro wird keine Werbung gezeigt.</p>
<h2>Käufe</h2><p>Pro wird über den App Store bzw. Google Play verkauft. Wir erhalten keine Zahlungsdaten, sondern nur die Information, ob Pro auf deinem Gerät aktiv ist.</p>
<h2>Vorlesen</h2><p>Fragen werden mit der Sprachausgabe deines Geräts vorgelesen. Die App nimmt keine Sprache auf.</p>
<h2>Deine Rechte</h2><p>Du hast das Recht auf Auskunft, Berichtigung, Löschung, Einschränkung der Verarbeitung, Datenübertragbarkeit, Widerspruch und Widerruf einer Einwilligung sowie das Recht, dich bei einer Datenschutz-Aufsichtsbehörde zu beschweren. Da wir selbst keine Daten über dich speichern, wende dich für Werbedaten an Google. Deinen Fortschritt löschst du unter Mehr › Fortschritt löschen oder indem du die App löschst.</p>
<h2>Änderungen</h2><p>Änderungen veröffentlichen wir auf dieser Seite.</p>
<hr><h1>Gizlilik Politikası</h1><p class="muted">{UPDATED['tr']}</p>
<p>Bu politika iPhone, iPad ve Android için LiD Trainer uygulamasını kapsar. Sorumlu: Asil Arslan, <a href="mailto:{MAIL}">{MAIL}</a>. Uygulama BAMF ya da başka bir kurum tarafından yayımlanmaz.</p>
<h2>Hesap ve sunucu yok</h2><p>Uygulamada giriş yoktur ve sunucu kullanmayız. İlerlemen, ayarların ve sınav sonuçların yalnızca cihazında ve yedeğinde saklanır.</p>
<h2>Reklam</h2><p>Ücretsiz sürümde Google AdMob, alıştırma ya da sınav provası sonunda reklam gösterir. Bunun için reklam kimliği, IP adresi, ondan çıkarılan yaklaşık konum ve reklam etkileşimleri işlenebilir. İlk açılışta Google'ın onay formu kişiselleştirilmiş reklama izin verip vermediğini sorar; izin vermezsen yalnızca kişiselleştirilmemiş reklam gösterilir. Seçimini istediğin an Daha fazla › Reklam gizlilik seçenekleri'nden değiştirebilir ya da geri çekebilirsin. Pro'da reklam yoktur.</p>
<h2>Satın alma</h2><p>Pro, App Store ya da Google Play üzerinden satılır. Ödeme bilgilerini almayız.</p>
<h2>Hakların</h2><p>Bilgi alma, düzeltme, silme, itiraz ve onayı geri çekme hakların vardır. Bizde senin hakkında veri yoktur; ilerlemeni Daha fazla › İlerlememi sil ile ya da uygulamayı silerek silebilirsin.</p>
<hr><div dir="rtl" lang="ar"><h1>سياسة الخصوصية</h1><p class="muted">{UPDATED['ar']}</p>
<p>تنطبق هذه السياسة على تطبيق LiD Trainer لأجهزة iPhone وiPad وAndroid. المسؤول: Asil Arslan، <a href="mailto:{MAIL}">{MAIL}</a>. لا يصدر التطبيق عن BAMF أو أي جهة رسمية.</p>
<h2>لا حسابات ولا خوادم</h2><p>لا يوجد تسجيل دخول ولا نستخدم خوادم. يُحفظ تقدمك وإعداداتك ونتائجك على جهازك ونسخته الاحتياطية فقط.</p>
<h2>الإعلانات</h2><p>تعرض النسخة المجانية إعلانات من Google AdMob بعد التمرين أو الاختبار التجريبي. قد تتم معالجة معرّف الإعلانات وعنوان IP والموقع التقريبي والتفاعل مع الإعلانات. يسألك نموذج الموافقة من Google عند أول تشغيل؛ وإذا رفضت تُعرض إعلانات غير مخصصة فقط. يمكنك تغيير اختيارك في أي وقت من المزيد › خيارات خصوصية الإعلانات. لا توجد إعلانات في Pro.</p>
<h2>المشتريات</h2><p>يُباع Pro عبر App Store أو Google Play، ولا نتلقى بيانات الدفع.</p>
<h2>حقوقك</h2><p>لك الحق في الاطلاع والتصحيح والحذف والاعتراض وسحب الموافقة. يمكنك حذف تقدمك من الإعدادات أو بحذف التطبيق.</p></div>"""

lid["terms"] = f"""<h1>Nutzungsbedingungen</h1><p class="muted">{UPDATED['de']} · Türkçe ve العربية aşağıda</p>
<p>LiD Trainer wird dir über den Store, aus dem du die App bezogen hast, zur persönlichen, nicht kommerziellen Nutzung nach dessen Standardbedingungen lizenziert (im App Store: Apples <a href="https://www.apple.com/legal/internet-services/itunes/dev/stdeula/">Standard-Endbenutzer-Lizenzvertrag</a>).</p>
<h2>Keine Behörden-App, keine Rechtsberatung</h2><p>LiD Trainer ist eine Lernhilfe. Die App wird nicht vom BAMF herausgegeben, ersetzt keine Rechtsberatung und garantiert nicht das Bestehen des Tests. Maßgeblich sind immer der amtliche Fragenkatalog und die Informationen der zuständigen Behörden. Die Übersetzungen ins Türkische und Arabische sind inoffiziell.</p>
<h2>Pro</h2><p>LiD Trainer Pro ist ein einmaliger In-App-Kauf, kein Abo. Erstattungen laufen über Apple bzw. Google nach deren Regeln.</p>
<h2>Die App</h2><p>Wir bemühen uns, die Inhalte richtig und aktuell zu halten, können aber Fehler nicht ausschließen. Dein Fortschritt liegt nur auf deinem Gerät; geht er verloren, können wir ihn nicht wiederherstellen.</p>
<h2>Rechte</h2><p>Code und Gestaltung der App gehören Asil Arslan. Fragen und Bilder stammen aus dem vom BAMF veröffentlichten Gesamtfragenkatalog; Wappen sind amtliche Hoheitszeichen der Länder und werden nur zur Darstellung der Prüfungsfragen gezeigt.</p>
<h2>Kontakt</h2><p><a href="mailto:{MAIL}">{MAIL}</a></p>
<hr><h1>Kullanım Koşulları</h1><p class="muted">{UPDATED['tr']}</p>
<p>LiD Trainer, edindiğin mağaza aracılığıyla ve o mağazanın standart koşullarına göre kişisel ve ticari olmayan kullanım için lisanslanır.</p>
<h2>Resmî değildir, hukuki danışmanlık değildir</h2><p>LiD Trainer bir çalışma aracıdır. BAMF tarafından yayımlanmaz, hukuki danışmanlık yerine geçmez ve sınavı geçeceğini garanti etmez. Her zaman resmî katalog ve yetkili kurumların bilgileri esastır. Türkçe ve Arapça çeviriler resmî değildir.</p>
<h2>Pro</h2><p>LiD Trainer Pro tek seferlik bir satın almadır, abonelik değildir. İadeler Apple ya da Google tarafından yürütülür.</p>
<h2>İletişim</h2><p><a href="mailto:{MAIL}">{MAIL}</a></p>
<hr><div dir="rtl" lang="ar"><h1>شروط الاستخدام</h1><p class="muted">{UPDATED['ar']}</p>
<p>يُرخَّص لك LiD Trainer للاستخدام الشخصي غير التجاري عبر المتجر الذي حصلت منه عليه ووفق شروطه القياسية.</p>
<h2>ليس تطبيقًا رسميًا ولا استشارة قانونية</h2><p>التطبيق أداة للدراسة، لا يصدر عن BAMF، ولا يغني عن الاستشارة القانونية، ولا يضمن النجاح. المرجع دائمًا هو الكتالوج الرسمي. الترجمات غير رسمية.</p>
<h2>Pro</h2><p>LiD Trainer Pro شراء لمرة واحدة وليس اشتراكًا. تتولى Apple أو Google طلبات الاسترداد.</p>
<h2>التواصل</h2><p><a href="mailto:{MAIL}">{MAIL}</a></p></div>"""
lid["titles"] = ("LiD Trainer", "LiD Trainer Support", "LiD Trainer Datenschutzerklärung", "LiD Trainer Nutzungsbedingungen")
lid["lang"] = "de"

for app in (civics, lid):
    out = os.path.join(SITE, app["slug"]); repo = os.path.expanduser(app["repo"])
    shutil.rmtree(out, ignore_errors=True); os.makedirs(f"{out}/assets")
    open(f"{out}/assets/styles.css", "w").write(CSS % app["css"])
    subprocess.run(["sips", "-Z", "256", os.path.join(repo, app["icon"]), "--out", f"{out}/assets/icon.png"], check=True, capture_output=True)
    folder, names = app["shots"]; imgs = []
    for n in names:
        dst = f"assets/{n[3:]}.jpg"
        subprocess.run(["sips", "-Z", "1000", "-s", "formatOptions", "75", os.path.join(repo, folder, n + ".jpg"), "--out", f"{out}/{dst}"], check=True, capture_output=True)
        imgs.append(f'<img src="{dst}" alt="" loading="lazy">')
    pages = [("", app["index"].replace("{shots}", "".join(imgs))), ("support", app["support"]), ("privacy-policy", app["privacy"]), ("terms-of-use", app["terms"])]
    for (sub, body), title in zip(pages, app["titles"]):
        d = os.path.join(out, sub); os.makedirs(d, exist_ok=True)
        open(f"{d}/index.html", "w").write(page(app, sub, title, body, app["lang"], bool(sub)))
    print(out)
