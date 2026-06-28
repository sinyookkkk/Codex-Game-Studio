$ErrorActionPreference = "Stop"

$ScriptDir = if ($PSScriptRoot) {
    $PSScriptRoot
} else {
    Split-Path -Parent $MyInvocation.MyCommand.Path
}

$RootDir = (Resolve-Path -LiteralPath (Join-Path -Path $ScriptDir -ChildPath "..")).Path
$Validator = Join-Path -Path $RootDir -ChildPath "scripts/validate_repository.py"

$PythonPath = $null
foreach ($Candidate in @("python3", "python")) {
    $Command = Get-Command $Candidate -ErrorAction SilentlyContinue
    if (-not $Command) {
        continue
    }

    & $Command.Source --version *> $null
    if ($LASTEXITCODE -eq 0) {
        $PythonPath = $Command.Source
        break
    }
}

if (-not $PythonPath) {
    Write-Error "Python 3 is required to validate this repository."
    exit 127
}

& $PythonPath $Validator @args
if ($null -eq $LASTEXITCODE) {
    exit 0
}
exit $LASTEXITCODE
