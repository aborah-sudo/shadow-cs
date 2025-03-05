import subprocess

def run_command(command):
    """Helper function to run shell commands."""
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return result

def test_useradd():
    """Test useradd command."""
    run_command("sudo useradd testuser")
    result = run_command("id testuser")
    if result.returncode == 0:
        print("Test 1: useradd - PASS")
    else:
        print("Test 1: useradd - FAIL")
    run_command("sudo userdel testuser")

def test_userdel():
    """Test userdel command."""
    run_command("sudo useradd testuser")
    run_command("sudo userdel testuser")
    result = run_command("id testuser")
    if result.returncode != 0:
        print("Test 2: userdel - PASS")
    else:
        print("Test 2: userdel - FAIL")

def test_usermod():
    """Test usermod command."""
    run_command("sudo useradd testuser")
    run_command("sudo usermod -d /home/newhome testuser")
    result = run_command("grep 'testuser.*/home/newhome' /etc/passwd")
    if result.returncode == 0:
        print("Test 3: usermod - PASS")
    else:
        print("Test 3: usermod - FAIL")
    run_command("sudo userdel -r testuser")

def test_groupadd():
    """Test groupadd command."""
    run_command("sudo groupadd testgroup")
    result = run_command("grep 'testgroup' /etc/group")
    if result.returncode == 0:
        print("Test 4: groupadd - PASS")
    else:
        print("Test 4: groupadd - FAIL")
    run_command("sudo groupdel testgroup")

def test_groupdel():
    """Test groupdel command."""
    run_command("sudo groupadd testgroup")
    run_command("sudo groupdel testgroup")
    result = run_command("grep 'testgroup' /etc/group")
    if result.returncode != 0:
        print("Test 5: groupdel - PASS")
    else:
        print("Test 5: groupdel - FAIL")

def test_passwd():
    """Test passwd command."""
    run_command("sudo useradd testuser")
    run_command("echo 'testuser:password' | sudo chpasswd")
    result = run_command("sudo grep 'testuser:' /etc/shadow")
    if result.returncode == 0:
        print("Test 6: passwd - PASS")
    else:
        print("Test 6: passwd - FAIL")
    run_command("sudo userdel -r testuser")

def test_chage():
    """Test chage command."""
    run_command("sudo useradd testuser")
    run_command("sudo chage -M 90 testuser")
    result = run_command("sudo chage -l testuser | grep 'Maximum number of days between password change.*90'")
    if result.returncode == 0:
        print("Test 7: chage - PASS")
    else:
        print("Test 7: chage - FAIL")
    run_command("sudo userdel -r testuser")

def test_gpasswd():
    """Test gpasswd command."""
    run_command("sudo useradd testuser")
    run_command("sudo groupadd testgroup")
    run_command("sudo gpasswd -a testuser testgroup")
    result = run_command("groups testuser | grep 'testgroup'")
    if result.returncode == 0:
        print("Test 8: gpasswd - PASS")
    else:
        print("Test 8: gpasswd - FAIL")
    run_command("sudo userdel -r testuser")
    run_command("sudo groupdel testgroup")


def test_chfn():
    """Test chfn command."""
    run_command("sudo useradd testuser")
    run_command("sudo chfn -f 'Test User' testuser")
    result = run_command("grep 'Test User' /etc/passwd")
    if result.returncode == 0:
        print("Test 10: chfn - PASS")
    else:
        print("Test 10: chfn - FAIL")
    run_command("sudo userdel -r testuser")

if __name__ == "__main__":
    test_useradd()
    test_userdel()
    test_usermod()
    test_groupadd()
    test_groupdel()
    test_passwd()
    test_chage()
    test_gpasswd()
    test_chfn()

