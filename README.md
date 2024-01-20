# Billboard Scraper Project

This project scrapes data from the Billboard Hot 100 chart and stores it in an SQLite database. It includes a Python script for web scraping, a PowerShell script for scheduling, and additional files for task automation.

## Files

- `billboard_scraper.py`: Python script for web scraping and database population.
- `schedule_task.ps1`: PowerShell script for scheduling the Python script using Task Scheduler.
- `README.md`: Project documentation.

## Setup

1. Install Python, Selenium, and BeautifulSoup: `pip install selenium beautifulsoup4`
2. Download the ChromeDriver executable and update the path in `billboard_scraper.py`.
3. Adjust paths in `schedule_task.ps1` to match your system.
4. Run `schedule_task.ps1` to schedule the weekly task.

## Usage

- Execute `billboard_scraper.py` manually or let the scheduled task run it weekly.

## Notes

- Ensure you have the necessary permissions for task scheduling.
- Review and modify scripts based on your specific requirements.
