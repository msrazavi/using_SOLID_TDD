# کاربرد عملی اصول شئ‌گرایی SOLID با استفاده از روش Test Driven Development
## توضیحات اجرای پروژه

در روش TDD نیاز است ابتدا خروجی‌های مطلوب به وسیله تست‌نویسی مشخص شوند. اینجا نیز در تست‌های واحد تمامی عملکردهای مورد انتظار برنامه را می‌نویسیم. سپس با رعایت اصول SOLID برنامه را پیاده‌سازی کرده و سپس تست‌ها را اجرا می‌کنیم و می‌بینیم که عملکرد برنامه مطابق حالت مطلوب است. اینجا چون برنامه تنها یک عملکرد اصلی دارد همه تست‌ها با هم نوشته شد ولی در برنامه‌های بزرگ‌تر باید برای هر بخش جداگانه TDD را انجام داد و مطابق اسم این روش، کاملا براساس تست‌ها پیش رفت. TDD کمک می‌کند که در هر بخش ریز از برنامه مطمئن شویم که خروجی مورد انتظار را می‌گیریم و با اطمینان از واحد‌های کوچک آن‌ها را به هم متصل کرده و استفاده کنیم و در باگ‌هایی که در سطوح بالاتر پیش می‌آید از درسی عملکرد سطوح اولیه مطمئن باشیم.

به بررسی هر یک از پنج اصل SOLID در پروژه می‌پردازیم:

**1. اصل تک مسئولیتی (Single Responsibility Principle)**

هر کلاس برای یک موضوع و مسئولیت تعریف شده است. کلاس مستطیل برای محاسبه مساحت و تغییر اندازه‌های یک مستطیل و کلاس مربع برای محاسبه مساحت و تغییر اندازه یک مربع. این تک‌وظیفگی باعث می‌شود تغییرات احتمالی که به موضوعات دیگر ربط دارند ما را ناچار به تغییر در کد این کلاس‌ها نکند.

**2.  اصل باز - بسته (Open/Closed Principle)**

 با طراحی کلاس‌های مستطیل و مربع به صورت بازبسته، برای افزودن یک شکل جدید به کد، نیازی به تغییر در این دو کلاس نیست و می‌توان با ایجاد یک کلاس جدید و از کلاس شکل ارث‌بری کردن، شکل جدید را پیاده‌سازی کرد. این کار باعث می‌شود که تغییر در یک کلاس، تاثیری بر سایر کلاس‌ها نداشته باشد. همچنین کلاس‌های مربع و مستطیل کاملا تست شده هستند و می‌توان به صورت بسته هر جا که لازم بود از آن‌ها استفاده کرد.

**3.  اصل جایگزینی لیسکوف (Liskov Substitution Principle)**

هر شیء از کلاس مربع یا مستطیل می‌تواند با یک شیء از کلاس شکل جایگزین شود و هیچ مشکلی پیش نیاید چون کلاس شکل هیچ ویژگی را پیاده سازی نمی‌کند که در مستطیل و مربع نباشد. اما طبیعی است که محاسبه مساحت این شکل نتیجه‌ای ندارد چون شکل و ابعادش باید برای محاسبه مساحت مشخص باشد ولی به ارور هم نمی‌خورد.

**4.  اصل جداسازی اینترفیس‌ها (Interface Segregation Principle)**

می‌توان گفت اینکه مستطیل و مربع هر دو به مفهوم انتزاعی‌تر شکل اشاره می‌کنند نوعی رعایت این اصل باشد.

**5.  اصل وارونگی وابستگی (Dependency Inversion Principle)**

این اصل نیز به طور ملموس در پروژه قابل مشاهده نیست اما به طور کلی کاهش وابستگی اجزای سطح بالا به اجزای سطح پایین را شامل می‌شود.

نکته‌ای در پیاده‌سازی: ابتدا کلاس مربع زیرکلاس مستطیل در نظر گرفته شد ولی با توجه به وجود setter ها و همچنین رعایت اصل LSP که در سوال آخر نیز توضیح داده شد دریافتیم بهتر است مربع نیز مستقلا از شکل ارث‌بری شود و نه از مستطیل.

## پرسش‌ها
### 1. هر یک از پنج اصل SOLID را در دو الی سه خط توضیح دهید.

**1. اصل تک مسئولیتی (Single Responsibility Principle)**

هر کلاس در برنامه فقط باید **یک دلیل** برای تغییر داشته باشد. می‌توان این را به این تعبیر کرد که هر کلاس باید یک وظیفه خاص داشته باشد. در واقع اهداف تابع‌هایی که در یک کلاس هستند باید کاملا با موضوع کلاس مربوط باشند. این اصل به جز در سطح کلاس در سطح تابع‌ها نیز باید رعایت شود به طوری که هر تابع فقط یک وظیفه خاص را انجام دهد. می‌توان وقتی یک کلاس توابع متعددی دارد که کارهای نامربوط انجام می‌دهند برای آن‌ها کلاس‌های جدید ایجاد کرد. رعایت این موضوع هنگام اضافه شدن فیچرهای جدید از تکرار کد و نیاز به تغییرات متعدد در کلاس‌های قبلی جلوگیری می‌کند.

**2.  اصل باز - بسته (Open/Closed Principle)**

 موجودیت‌های یک نرم‌افزارمانند کلاس‌ها و توابع و ماژول‌ها باید برای توسعه داده شدن باز و برای تغییر دادن بسته باشد. منظور از باز بودن برای توسعه این است که بتوان ویژگی‌ها و توابع جدید به کلاس افزود بدون اینکه عملکرد کلاس مخدوش بشود یا به عملکرد سایر کلاس‌هایی که با این کلاس ارتباط دارند آسیب وارد بشود. منظور از بسته بودن در برابر تغییر نیز این است که کلاس مورد نظر ۱۰۰ درصد تست شده باشد و درست کار کند و برای اضافه کردن قابلیت‌های جدید نیاز نباشد در کد زده شده تغییر داخلی ایجاد کرد و تنها با اضافه کردن آن را توسعه داد.
 
**3.  اصل جایگزینی لیسکوف (Liskov Substitution Principle)**

این اصل می‌گوید اگر یک کلاس زیرکلاس کلاس دیگر باشد، نمونه‌های نوع پدر باید بتوانند بدون هیچ تغییری در کد با نمونه‌هایی از نوع فرزند جایگزین شوند. به زبان دیگر هیچ کلاس فرزندی نباید حین اورراید کردن از کلاس پدر ویژگی‌های اشیا پدر را تغییر بدهد یا نقض کند به طوری که عملکرد و نوع خروجی متفاوت شود چون در این صورت با جایگزینی شیء پدر با شیء فرزند به عملکرد غیر قابل انتظاری برمی‌خوریم.

**4.  اصل جداسازی اینترفیس‌ها (Interface Segregation Principle)**

  هیچ کلاسی نباید به ناچار تابعی که هیچ نیازی به آن ندارد را پیاده‌سازی کند. راهکاری که برای جلوگیری از این موضوع وجود دارد این است که اینترفیس‌ها را از هم جدا کنیم به طوری که توابعی که در کلاس‌های مختلف کاربرد دارند در یک اینترفیس کنار هم نباشند. این اصل نیز مانند سایر اصول SOLID باعث خوانایی بیشتر و قابلیت ریفکتور ساده‌تر می‌شود.
  
**5.  اصل وارونگی وابستگی (Dependency Inversion Principle)**

کلاس‌ها و ماژول‌های سطح بالاتر نباید هیچ وابستگی به موجودیت‌های سطح پایین‌تر داشته باشند. بلکه همه کلاس‌ها باید به موجودیت‌های انتزاعی وابسته باشند که از جزئیات مستقل است. منظور از کلاس سطح بالا کلاسی است که عملیات پیچیده‌ای را با استفاده از توابع کلاس سطح پایین انجام می‌دهد و کلاس سطح پایین معمولا کارهای پایه‌ای مثل اتصال به دیتابیس یا عملیات فایل و... انجام می‌دهد. موجودیت‌های انتزاعی هم یک کلاس غیر قابل نمونه گیری است که بقیه کلاس‌ها فرزند آن هستند.


### 2. اصول SOLID در کدام یک از گام‌های اصلی ایجاد نرم‌افزار (تحلیل نیازمندی‌ها، طراحی، پیاده‌سازی، تست و استقرار) استفاده می‌شوند؟ توضیح دهید.

می‌توان گفت در تمام گام‌های اصلی باید این اصول رعایت شوند. اصل SRP باید در طراحی مورد نظر قرار گیرد و برای هر یک از کلاس‌های طراحی شده تنها یک کار در نظر گرفته شود. اصل OCP هم در طراحی و هم در پیاده‌سازی باید رعایت شود چون برخی جزئیات که کلاس را نسبت به تغییرات بسته می‌کند تنها در پیاده‌سازی قابل بررسی است و قسمت اعظم رعایت همه اصول هم به طراحی برمیگردد. اصل LSP نیز علاوه بر طراحی قسمت عمده‌اش در پیاده‌سازی باید مورد توجه قرار گیرد. اصل ISP تقریبا فقط در طراحی مهم است و همانجا اینترفیس‌ها و توابعی که شامل می‌شوند مشخص می‌شود. و در آخر اصل DIP نیز بخش اصلی‌اش در طراحی و رعایت جزئی از آن به پیاده‌سازی برمی‌گردد.
پس به طور کلی در مرحله طراحی باید همه اصول را در نظر گرفت و در مرحله پیاده‌سازی نیز باید برخی اصول مثل OCP و LSP در راستای طراحی درستی که داشته‌اند مد نظر قرار گیرند تا جزئیات نیز اصول را نقض نکنند.
در گام تست ممکن است به باگ‌های ایجاد شده توسط نقض اصول SOLID بربخوریم و باید در اصلاح طراحی و پیاده‌سازی به رعایت این اصول بپردازیم.

### 3. در چرخه‌ی عمومی ایجاد نرم‌افزار، آزمون نرم‌افزار دیرتر از پیاده‌سازی نرم‌افزار انجام می‌شود، اما در روش TDD تست‌نویسی پیش از پیاده‌سازی شروع می‌شود. آیا این دو مورد با هم تناقضی دارند؟ توضیح دهید.

خیر تناقضی ندارند. زیرا این تست‌نویسی که در TDD پیش از پیاده‌سازی انجام می‌شود آزمودن عملکرد برنامه نیست بلکه مشخص کردن دقیق عملکرد مطلوب برنامه است. و گام تست که در چرخه عمومی نرم‌افزار بعد از پیاده‌سازی قرار دارد اینجا نیز بعد از پیاده‌سازی قرار دارد و اجرای آن تست‌های نوشته شده است که مشخص می‌کند آیا برنامه پیاده شده آن عملکرد مورد انتظار را دارد یا خیر. در حقیقت اگر بخواهیم مراحل TDD را به گونه‌ای با چرخه عمومی ایجاد نرم‌افزار منطبق کنیم می‌توان گفت تست‌نویسی اولیه را می‌توان بخشی از پیاده‌سازی یا حتی طراحی شمرد که مشخص‌کننده جزئیات خواسته شده از هر قسمت از برنامه است.

### 4. فرض کنید در آزمایش بالا نیازی به تغییر ابعاد مستطیل نداشتیم. آیا در این حالت می‌توانستیم مربع را از مستطیل به ارث ببریم؟ توضیح دهید.

اگر مطمئن بودیم همیشه برنامه ثابت خواهد ماند شاید می‌توانستیم این کار را کنیم چون مربع یک مستطیل است. ولی برفرض اینکه میخواستیم یک ویژگی به مستطیل اضافه کنیم که وابسته به تفاوت میان مربع و مستطیل بود آنگاه اصل LSP از اصول SOLID نقض میشد. تفاوت میان مستطیل و مربع همین است که وقتی طول مستطیلی که مربع است عوض می‌شود باید عرضش هم عوض بشود و برعکس.

یعنی اگر یک شیء از مستطیل را با یک شیء از مربع جایگزین می‌کردیم و اقدام به تغییر طول یا عرض آن می‌کردیم باید همه اضلاع تغییر می‌کردند در حالی که در توابع setter مستطیل این امکان فراهم نبود.

اما اگر این نیاز به تغییر ابعاد را نداشتیم در حالت فعلی برنامه شاید می‌توانستیم این ارث‌بری را انجام دهیم و مشکلی در ظاهر پیش نیاید اما برای رعایت بهتر اصول SOLID مخصوصا LSP و ISP بهتر است استقلال کلاس‌ها را حفظ کنیم و هر دو را وابسته به یک پدر اصلی و مشترک که شکل باشد بکنیم.
