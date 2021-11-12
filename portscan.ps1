[CmdletBinding()] param([Parameter()] [string] $ip)
$ports = @(444..447)
foreach ($p in $ports){
    $r = tnc $ip -port $p | out-string -Stream
    [string]$re = $r | Select-String -Pattern 'TcpTestSucceeded'| Select-String -Pattern 'True'
    if ($re -eq "TcpTestSucceeded : True"){
        Write-Host "Puerto Abierto: " -NoNewline; Write-Host $p -ForegroundColor Green
    }

}