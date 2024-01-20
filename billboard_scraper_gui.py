import sqlite3
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import tkinter as tk
from tkinter import messagebox

class BillboardScraperGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Billboard Scraper")

        self.label = tk.Label(self.master, text="Click the button to scrape Billboard Hot 100")
        self.label.pack(pady=10)

        self.scrape_button = tk.Button(self.master, text="Scrape Data", command=self.scrape_and_store)
        self.scrape_button.pack(pady=10)

    def scrape_and_store(self):
        try:
            # provide your chromedriver path below
            driver = webdriver.Chrome(executable_path='/path/to/chromedriver')
            driver.get('https://www.billboard.com/charts/hot-100/')

            soup = BeautifulSoup(driver.page_source, 'html.parser')
            songs = soup.find_all('span', class_='chart-element__information')

            conn = sqlite3.connect('billboard_data.db')
            cursor = conn.cursor()

            # Create a table if it doesn't exist
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS billboard_chart (
                    id INTEGER PRIMARY KEY,
                    title TEXT,
                    artist TEXT,
                    week_date DATE
                )
            ''')

            # Get the current week's date
            current_week_date = datetime.now().strftime('%Y-%m-%d')

            # Delete data older than the last 4 weeks
            oldest_week_date = (datetime.now() - timedelta(weeks=4)).strftime('%Y-%m-%d')
            cursor.execute('DELETE FROM billboard_chart WHERE week_date < ?', (oldest_week_date,))

            # Insert new data with the current week's date
            for song in songs:
                title = song.find('span', class_='chart-element__information__song').get_text(strip=True)
                artist = song.find('span', class_='chart-element__information__artist').get_text(strip=True)

                cursor.execute('INSERT INTO billboard_chart (title, artist, week_date) VALUES (?, ?, ?)',
                               (title, artist, current_week_date))

            # Commit and close connections
            conn.commit()
            conn.close()
            driver.quit()

            messagebox.showinfo("Success", "Data scraped and stored successfully!")

        except WebDriverException as e:
            messagebox.showerror("Error", f"Error: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = BillboardScraperGUI(root)
    root.mainloop()
