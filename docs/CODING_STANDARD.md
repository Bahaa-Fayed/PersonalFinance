# Coding Standard

## Python

- الالتزام بمعيار PEP8.
- استخدام أسماء باللغة الإنجليزية.
- أسماء المتغيرات بصيغة snake_case.
- أسماء الـ Classes بصيغة PascalCase.
- أسماء الثوابت UPPER_CASE.
- كتابة Type Hints كلما أمكن.
- كتابة Docstrings لكل Class وFunction عامة.
- عدم استخدام Magic Numbers.
- عدم تكرار الكود (DRY).
- الالتزام بمبدأ المسؤولية الواحدة (SRP).

---

## HTML

- استخدام HTML5.
- دعم RTL.
- استخدام عناصر Semantic HTML.
- تجنب Inline CSS.

---

## CSS

- Mobile First.
- استخدام Bootstrap أولاً.
- تخصيص CSS في ملفات منفصلة.
- عدم استخدام !important إلا عند الضرورة.

---

## JavaScript

- استخدام ES6+.
- عدم استخدام jQuery إلا عند الحاجة.
- فصل منطق الصفحة عن واجهة المستخدم.

---

## Git

- Commit صغير وواضح.
- رسالة Commit تصف تغييرًا واحدًا.
- كل ميزة في Branch مستقل.
- مراجعة الكود قبل الدمج.

---

## Database

- جميع العمليات تتم عبر SQLAlchemy.
- يمنع تنفيذ SQL خام إلا للضرورة.
- دعم SQLite وPostgreSQL.

---

## Documentation

أي Class جديد يجب أن يوثق.

أي Feature جديدة يجب إضافتها إلى ROADMAP وCHANGELOG.

---

## Testing

كل Feature مهمة يجب أن يكون لها Test لاحقًا.
