# Decompile with IDA

#/* Decompile_Code */
'''
int __cdecl main(int argc, const char **argv, const char **envp)
{
  char v4[256]; // [rsp+20h] [rbp-118h] BYREF

  memset(v4, 0, sizeof(v4));
  sub_140001190("Input : ", argv, envp);
  sub_1400011F0("%256s", v4);
  if ( sub_140001000(v4) )
    puts("Correct");
  else
    puts("Wrong");
  return 0;
}

_BOOL8 __fastcall sub_140001000(const char *a1)
{
  return strcmp(a1, "Compar3_the_str1ng") == 0;
}
'''

'''
=========================================================
DH{Compar3_the_str1ng}
=========================================================
'''