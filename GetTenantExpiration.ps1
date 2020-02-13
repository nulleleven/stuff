Param
(
[string]$tenantEmail,
[string]$tenantPassword
)

[hashtable]$Return = @{}
$subExp = New-Object Collections.Generic.List[string]

$pass = ConvertTo-SecureString $tenantPassword -AsPlainText -Force
$creds = New-Object System.Management.Automation.PsCredential($tenantEmail, $pass)

Connect-MsolService -Credential $creds

$account = Login-AzureRmAccount -Credential $creds
$subs = Get-MsolSubscription -TenantId $account.Context.Tenant.Id
foreach ($s in $subs){
    $subExp.Add($s.NextLifeCycleDate.ToString())
}

$Return.ExpirationDates = [string[]]$subExp
$Return.Email = [string]$tenantEmail
$Return.Password = [string]$tenantPassword

return $Return