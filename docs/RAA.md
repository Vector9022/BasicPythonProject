## `IsAdmin` 📝 Проверяет запущен ли процесс с правами администратора. [[Назад](Main.md)]

### ⚙️ Параметры
- `return`[bool] - Возвращает значение True если процесс с правами администратора или False если нет.

### 🔍 Пример использования
```python
import localLib.RAA as RAA

result = RAA.IsAdmin()
print(result) > True/False
```
<hr><br>



## `RunAsAdmin` 📝 Перезапускает текущий процесс с правами администратора. [[Назад](Main.md)]

> ### 💡 Примечание
> Если уже админ ничего не делает.

### 🔍 Пример использования
```python
import localLib.RAA as RAA

RAA.RunAsAdmin()
```
<hr><br>