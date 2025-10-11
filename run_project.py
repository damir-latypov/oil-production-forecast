"""
Скрипт для автоматического запуска проекта
"""
import subprocess
import sys
import os

def run_command(command, description):
    """Запускает команду и выводит описание"""
    print(f"\n{'='*50}")
    print(f"🚀 {description}")
    print(f"{'='*50}")
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"❌ Ошибка: {result.stderr}")
        return False
    print("✅ Успешно выполнено")
    return True

def main():
    print("🛢️ ЗАПУСК ПРОЕКТА ПРОГНОЗА ДЕБИТА НЕФТЯНЫХ СКВАЖИН")
    print("="*60)
    
    # Создаем папки
    folders = ['images', 'results', 'data', 'models']
    for folder in folders:
        if not os.path.exists(folder):
            os.makedirs(folder)
            print(f"✅ Создана папка: {folder}")
    
    # Устанавливаем зависимости
    if not run_command("pip install -r requirements.txt", "Установка зависимостей"):
        return
    
    # Запускаем основной скрипт
    if not run_command("python oil_production_forecast.py", "Запуск основного скрипта"):
        return
    
    print("\n🎉 ПРОЕКТ УСПЕШНО ЗАПУЩЕН!")
    print("📁 Результаты сохранены в папках:")
    print("   • models/ - лучшая модель")
    print("   • results/ - метрики и сравнения")
    print("   • images/ - графики и визуализации")

if __name__ == "__main__":
    main()
