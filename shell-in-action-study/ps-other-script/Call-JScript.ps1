function Call-JScript
{
    $sc = New-Object -ComObject ScriptControl
    $sc.Language = 'JScript'
    $sc.AddCode('
        function getLength(s) {
            return s.length;
        }
        function Add(x, y) {
            return x + y;
        }
    ')
    $sc.CodeObject
}

$js = Call-JScript
