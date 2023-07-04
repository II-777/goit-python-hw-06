# goit-python-hw-06

#  Завдання
## Функція normalize:

1. Здійснює транслітерацію кириличного алфавіту на латинський.
2. Замінює всі символи крім латинських літер, цифр на '_'.

Вимоги до функції normalize:

+ приймає на вхід рядок та повертає рядок;
+ здійснює транслітерацію кириличних символів на латиницю;
+ замінює всі символи, крім літер латинського алфавіту та цифр, на символ '_';
+ транслітерація може не відповідати стандарту, але бути читабельною;
+ великі літери залишаються великими, а маленькі — маленькими після транслітерації.

## Умови для обробки:

- зображення переносимо до папки images
- документи переносимо до папки documents
- аудіо файли переносимо до audio
- відео файли до video
- архіви розпаковуються та їх вміст переноситься до папки archives

# Критерії приймання завдання

+всі файли та папки перейменовуються за допомогою функції normalize.
+розширення файлів не змінюється після перейменування.
-порожні папки видаляються
-скрипт ігнорує папки archives, video, audio, documents, images;
-розпакований вміст архіву переноситься до папки archives у підпапку, названу так само, як і архів, але без розширення в кінці;
-файли, розширення яких невідомі, залишаються без зміни.

## Завдання

У багатьох на робочому столі є папка, яка називається якось на кшталт "Розібрати". Як правило, розібрати цю папку руки ніколи так і не доходять.

Ми з вами напишемо скрипт, який розбере цю папку. Зрештою ви зможете налаштувати цю програму під себе і вона виконуватиме індивідуальний сценарій, що відповідає вашим потребам. Для цього наш застосунок буде перевіряти розширення файлу (останні символи в імені файлу, як правило, після крапки) і, залежно від розширення, приймати рішення, до якої категорії віднести цей файл.

Скрипт приймає один аргумент під час запуску — це ім'я папки, в якій він буде здійснювати сортування. Припустимо, що файл з програмою називається sort.py, тоді, щоб відсортувати папку /user/Desktop/Мотлох, потрібно запустити скрипт командою python sort.py /user/Desktop/Мотлох

	- Для того щоб успішно впоратися з цим завданням, ви повинні винести логіку обробки папки в окрему функцію.
	- Щоб скрипт міг пройти на будь-яку глибину вкладеності, функція обробки папок повинна рекурсивно викликати сама себе, коли їй зустрічаються вкладенні папки.

Скрипт повинен проходити по вказаній під час виклику папці та сортирувати всі файли за групами:

- зображення ('JPEG', 'PNG', 'JPG', 'SVG');
- відео файли ('AVI', 'MP4', 'MOV', 'MKV');
- документи ('DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX');
- музика ('MP3', 'OGG', 'WAV', 'AMR');
- архіви ('ZIP', 'GZ', 'TAR');
- невідомі розширення.

Ви можете розширити та доповнити цей список, якщо хочете.

В результатах роботи повинні бути:

- Список файлів в кожній категорії (музика, відео, фото та ін.)
- Перелік усіх відомих скрипту розширень, які зустрічаються в цільовій папці.
- Перелік всіх розширень, які скрипту невідомі.

Потім необхідно додати функції, які будуть відповідати за обробку кожного типу файлів.

Крім того, всі файли та папки потрібно перейменувати, видаливши із назви всі символи, що призводять до проблем. Для цього потрібно застосувати до імен файлів функцію normalize. Варто розуміти, що перейменувати файли потрібно так, щоб не змінити розширення файлів.

# Функція normalize:

1. Здійснює транслітерацію кириличного алфавіту на латинський.
2. Замінює всі символи крім латинських літер, цифр на '_'.

Вимоги до функції normalize:

- приймає на вхід рядок та повертає рядок;
- здійснює транслітерацію кириличних символів на латиницю;
- замінює всі символи, крім літер латинського алфавіту та цифр, на символ '_';
- транслітерація може не відповідати стандарту, але бути читабельною;
- великі літери залишаються великими, а маленькі — маленькими після транслітерації.

## Умови для обробки:

- зображення переносимо до папки images
- документи переносимо до папки documents
- аудіо файли переносимо до audio
- відео файли до video
- архіви розпаковуються та їх вміст переноситься до папки archives

# Критерії приймання завдання

-всі файли та папки перейменовуються за допомогою функції normalize.
-розширення файлів не змінюється після перейменування.
-порожні папки видаляються
-скрипт ігнорує папки archives, video, audio, documents, images;
-розпакований вміст архіву переноситься до папки archives у підпапку, названу так само, як і архів, але без розширення в кінці;
-файли, розширення яких невідомі, залишаються без зміни.
