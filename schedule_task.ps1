# schedule_task.ps1

# Set the path to the Python executable and the Python script
$pythonPath = "C:\Path\To\Python\python.exe"
$scriptPath = "C:\Path\To\Your\Python\Script.py"

# Set the path to the PowerShell script
$psScriptPath = "C:\Path\To\Your\schedule_script.ps1"

# Set the task name and description
$taskName = "BillboardScraperTask"
$taskDescription = "Task to run Billboard Scraper script weekly"

# Create a new scheduled task
$action = New-ScheduledTaskAction -Execute "$pythonPath" -Argument "$scriptPath"
$trigger = New-ScheduledTaskTrigger -Weekly -At "3:00 PM" -DaysOfWeek Sunday  # Adjust the time and day as needed
Register-ScheduledTask -Action $action -Trigger $trigger -TaskName $taskName -Description $taskDescription

# Run the PowerShell script to schedule the task
Start-Process -FilePath "powershell.exe" -ArgumentList "-File $psScriptPath"
