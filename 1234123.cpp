std::vector<DWORD> pids;
std::wstring targetProcessName = L”notepad.exe”;
 
HANDLE snap = CreateToolhelp32Snapshot(TH32CS_SNAPPROCESS, 0); //all processes
 
PROCESSENTRY32W entry; //current process
entry.dwSize = sizeof entry;
 
if (!Process32FirstW(snap, &entry)) { //start with the first in snapshot
return 0;
}
 
do {
if (std::wstring(entry.szExeFile) == targetProcessName) {
pids.emplace_back(entry.th32ProcessID); //name matches; add to list
}
} while (Process32NextW(snap, &entry)); //keep going until end of snapshot
 
for (int i(0); i < pids.size(); ++i) {
std::cout << pids[i] << std::endl;
}