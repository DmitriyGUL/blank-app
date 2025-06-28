<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Группы</title>
    <style>
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        
        body {
            background: linear-gradient(135deg, #6a11cb 0%, #2575fc 100%);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }
        
        .container {
            background: rgba(255, 255, 255, 0.9);
            border-radius: 20px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
            width: 100%;
            max-width: 500px;
            padding: 40px;
            text-align: center;
        }
        
        .logo {
            width: 120px;
            height: 120px;
            background: linear-gradient(45deg, #6a11cb, #2575fc);
            border-radius: 50%;
            margin: 0 auto 30px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 50px;
            color: white;
            font-weight: bold;
        }
        
        h1 {
            color: #333;
            margin-bottom: 30px;
            font-size: 28px;
        }
        
        .input-group {
            margin-bottom: 25px;
        }
        
        input {
            width: 100%;
            padding: 15px 20px;
            border: 2px solid #ddd;
            border-radius: 50px;
            font-size: 16px;
            transition: all 0.3s;
        }
        
        input:focus {
            border-color: #6a11cb;
            outline: none;
            box-shadow: 0 0 0 3px rgba(106, 17, 203, 0.2);
        }
        
        .btn {
            background: linear-gradient(to right, #6a11cb, #2575fc);
            color: white;
            border: none;
            padding: 15px 40px;
            font-size: 18px;
            border-radius: 50px;
            cursor: pointer;
            transition: all 0.3s;
            font-weight: 600;
            box-shadow: 0 4px 15px rgba(106, 17, 203, 0.3);
        }
        
        .btn:hover {
            transform: translateY(-3px);
            box-shadow: 0 7px 20px rgba(106, 17, 203, 0.4);
        }
        
        .btn:active {
            transform: translateY(-1px);
        }
        
        .toast {
            position: fixed;
            bottom: 20px;
            left: 50%;
            transform: translateX(-50%);
            background: #333;
            color: white;
            padding: 15px 25px;
            border-radius: 50px;
            opacity: 0;
            transition: opacity 0.3s;
        }
        
        .toast.show {
            opacity: 1;
        }
        
        @media (max-width: 600px) {
            .container {
                padding: 30px 20px;
            }
            
            .logo {
                width: 100px;
                height: 100px;
                font-size: 40px;
            }
            
            h1 {
                font-size: 24px;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="logo">G</div>
        <h1>Создайте новую группу</h1>
        
        <div class="input-group">
            <input 
                type="text" 
                id="groupName" 
                placeholder="Введите название группы"
                maxlength="50"
            >
        </div>
        
        <button class="btn" id="inviteBtn">Пригласить</button>
    </div>
    
    <div class="toast" id="toast">Ссылка скопирована в буфер!</div>

    <script>
        document.addEventListener('DOMContentLoaded', () => {
            const groupNameInput = document.getElementById('groupName');
            const inviteBtn = document.getElementById('inviteBtn');
            const toast = document.getElementById('toast');
            
            inviteBtn.addEventListener('click', () => {
                const groupName = groupNameInput.value.trim();
                
                if (!groupName) {
                    groupNameInput.focus();
                    groupNameInput.style.borderColor = '#ff4757';
                    setTimeout(() => {
                        groupNameInput.style.borderColor = '#ddd';
                    }, 2000);
                    return;
                }
                
                // Генерация уникального ID группы (в реальном приложении должен быть с бэкенда)
                const groupId = generateGroupId();
                
                // Создание ссылки-приглашения
                const inviteLink = `${window.location.origin}/join?group=${encodeURIComponent(groupName)}&id=${groupId}`;
                
                // Копирование в буфер обмена
                navigator.clipboard.writeText(inviteLink).then(() => {
                    showToast();
                });
            });
            
            function generateGroupId() {
                return 'group-' + Math.random().toString(36).substr(2, 9);
            }
            
            function showToast() {
                toast.classList.add('show');
                setTimeout(() => {
                    toast.classList.remove('show');
                }, 3000);
            }
            
            // Обработка нажатия Enter в поле ввода
            groupNameInput.addEventListener('keypress', (e) => {
                if (e.key === 'Enter') {
                    inviteBtn.click();
                }
            });
        });
    </script>
</body>
</html>
