# tipe data dictionary

member1 = {
    "ID": 101,
    "Nama": "Danil syah",
    "Pekerjaan": "Mahasiswa",
    "Status member": "Gold"
}
member2 = {
    "ID": 102,
    "Nama": "Haykal",
    "Pekerjaan": "Profesor",
    "Status member": "Berlian"
}


memberList = {101: member1, 102: member2}
print(memberList[102])


print(member1)
print(member1["Nama"])
print(member1.keys())
print(member1.values())
print(member1.items())
