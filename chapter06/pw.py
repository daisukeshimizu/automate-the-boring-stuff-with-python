#! python3
# pw.py - パスワード管理プログラム(脆弱性あり)

PASSWORD = { 'email' : 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
			 'blog' : 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
			 'luggage' : '12345' }

import sys
import pyperclip

if len(sys.argv) < 2:
	print('使い方: python3 pw.py [アカウント名]')
	print('パスワードをクリップボードにコピーします')
	sys.exit()

account = sys.argv[1] # 最初のコマンドライン引数がアカウント名

if account in PASSWORD:
	pyperclip.copy(PASSWORD[account])
	print(account + 'のパスワードをクリップボードにコピーしました')
else:
	print(account + 'というアカウント名はありません')

