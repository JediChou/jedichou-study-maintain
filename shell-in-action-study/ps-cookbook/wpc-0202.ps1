<#
  OReilly-Windows PowerShell Cookbook, 3rd edition
  Author: Lee Holmes
  Chaper 2.2. Group and Pivot Data by Name
  Problem:
    You want to easily access items in a list by a property name.
#>

$h = dir | group -AsHash -AsString Length
$h
