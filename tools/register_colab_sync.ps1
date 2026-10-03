<#
.SYNOPSIS
Register or update the single canonical Cygnus-Colab-Sync Windows scheduled task.
.DESCRIPTION
Uses the signed-in user's Python/rclone environment. No password is stored.
Daily at 09:00 machine local time (this workstation is UTC+08:00, matching Manila).
Update this task in place; never create per-batch schedules. Run with -VerifyOnly
to inspect it without registration. The task runs Python directly, without Codex.
#>
[CmdletBinding()]
param([switch]$VerifyOnly)

$ErrorActionPreference = 'Stop'
Set-StrictMode -Version Latest
$taskName = 'Cygnus-Colab-Sync'
$taskPath = '\'
if ($VerifyOnly) {
    Get-ScheduledTask -TaskName $taskName -TaskPath $taskPath | Select-Object TaskName, State, Actions, Triggers, Settings, Principal
    Get-ScheduledTaskInfo -TaskName $taskName -TaskPath $taskPath
    exit 0
}

$repoRoot = (Resolve-Path -LiteralPath (Split-Path -Parent $PSScriptRoot)).Path
$pythonExe = (Get-Command python.exe -ErrorAction Stop).Source
$pythonWindowless = Join-Path -Path (Split-Path -Parent $pythonExe) -ChildPath 'pythonw.exe'
if (-not (Test-Path -LiteralPath $pythonWindowless)) { throw 'pythonw.exe is required for a windowless task' }
Get-Command rclone.exe -ErrorAction Stop | Out-Null
$userName = [Security.Principal.WindowsIdentity]::GetCurrent().Name
$action = New-ScheduledTaskAction -Execute $pythonWindowless -WorkingDirectory $repoRoot -Argument '-m cygnus.colab_sync --all --update-notes --log state/colab_sync/latest.json'
$trigger = New-ScheduledTaskTrigger -Daily -At '09:00'
$principal = New-ScheduledTaskPrincipal -UserId $userName -LogonType Interactive -RunLevel Limited
$settings = New-ScheduledTaskSettingsSet -StartWhenAvailable -WakeToRun -MultipleInstances IgnoreNew -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -ExecutionTimeLimit (New-TimeSpan -Hours 1) -RestartCount 2 -RestartInterval (New-TimeSpan -Minutes 15)
$definition = New-ScheduledTask -Action $action -Trigger $trigger -Principal $principal -Settings $settings -Description 'Canonical Ad Astra Colab tier-input sync. Discover Cygnus/colab_runs; verify metadata; update repo notes. Reuse this task; no Codex dependency. See docs/COLAB_SYNC.md.'
Register-ScheduledTask -TaskName $taskName -TaskPath $taskPath -InputObject $definition -Force | Out-Null
Get-ScheduledTask -TaskName $taskName -TaskPath $taskPath | Select-Object TaskName, State, Actions, Principal
Get-ScheduledTaskInfo -TaskName $taskName -TaskPath $taskPath
