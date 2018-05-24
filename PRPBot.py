import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import random
from math import sqrt
import json

bot = Bot(command_prefix="+")
message = "Total damage: "
message2 = "Total damage: "
message3 = ""
statusmessage = ""
partyGauge = 0

with open('skills.json') as file:
	skills = json.load(file)
with open('characters.json') as file:
	characters = json.load(file)
with open('xp.json') as file:
	xpcurve = json.load(file)
with open('personas.json') as file:
	personas = json.load(file)
with open('personas2.json') as file:
	personas2 = json.load(file)
	
with open('characters/joshkinz.json') as file:
	joshkinz = json.load(file)
with open('characters/crying.json') as file:
	crying = json.load(file)
with open('characters/liminori.json') as file:
	liminori = json.load(file)
with open('characters/swiggle.json') as file:
	swiggle = json.load(file)
	
with open('characters/shadowjoe323.json') as file:
	shadowjoe323 = json.load(file)
with open('characters/lord_thantus.json') as file:
	lord_thantus = json.load(file)
with open('characters/qlonever.json') as file:
	qlonever = json.load(file)
with open('characters/nintendofan.json') as file:
	nintendofan = json.load(file)
	
characterlist = ['joshkinz', 'crying', 'liminori', 'swiggle', 'shadowjoe323', 'lord_thantus', 'qlonever', 'nintendofan']
lawlist = ['joshkinz', 'crying', 'liminori', 'swiggle', 'ultramario1998']
chaoslist = ['shadowjoe323', 'lord_thantus', 'qlonever', 'nintendofan']
enemylist = ['Pixie', 'Pyro Jack', 'Silky', 'Agathion', 'Mandrake', 'Nekomata']
magiclist = ['zio', 'zionga', 'ziodyne', 'thunderreign', 'agi', 'agilao', 'agidyne', 'inferno', 'garu', 'garula', 'garudyne', 'pantarhei', 'bufu', 'bufula', 'bufudyne', 'diamonddust']
itemhpsetlist = ['recovr50', 'recovr100']
itemhppercentlist = ['lifestone', 'bead']

@bot.event
async def on_ready():
	print('Logged in as')
	print(bot.user.name)
	print(bot.user.id)
	print('------')

@bot.command(name="attack", pass_context = True)
async def _attack(ctx, endef, name='a'):
	global message
	global partyGauge
	global message3
	
	if name.lower() == "lucas":
		name = "joshkinz"
	if name.lower() == "wes":
		name = "crying"
	if name.lower() == "dorothy":
		name = "liminori"
	if name.lower() == "limi":
		name = "liminori"
	if name.lower() == "bailey":
		name = "swiggle"
	if name.lower() == "ash":
		name = "shadowjoe323"
	if name.lower() == "joe":
		name = "shadowjoe323"
	if name.lower() == "shadowjoe":
		name = "shadowjoe323"
	if name.lower() == "arlo":
		name = "lord_thantus"
	if name.lower() == "thantus":
		name = "lord_thantus"
	if name.lower() == "quentin":
		name = "qlonever"
	if name.lower() == "qlon":
		name = "qlonever"
	if name.lower() == "emily":
		name = "nintendofan"
	if name.lower() == "nfan":
		name = "nintendofan"
		
	if endef not in characterlist:
		if name == 'a':
			hp = personas[str(endef)]['currenthp']
		if not name == 'a':	
			hp = personas[str(endef)]['currenthp']
			sp = personas[str(endef)]['currentsp']
	if endef in characterlist:
		hp = personas[str(endef)]['currenthp']
		sp = personas[str(endef)]['currentsp']
	
	if endef in characterlist:
		if ctx.message.author.name.lower() not in characterlist:
			strn = personas[str(endef)]['strength']
			atk = personas[str(endef)]['weaponatk']
			end = eval(name)['endurance']
	if endef not in characterlist:
		if not ctx.message.author.server_permissions.administrator:
			strn = eval(ctx.message.author.name.lower())['strength']
			atk = eval(ctx.message.author.name.lower())['weaponatk']
		if ctx.message.author.server_permissions.administrator:
			if not ctx.message.author.name.lower() == "joshkinz":
				strn = eval(name.lower())['strength']
				atk = eval(name.lower())['weaponatk']
			if ctx.message.author.name.lower() == "joshkinz":
				strn = eval(ctx.message.author.name.lower())['strength']
				atk = eval(ctx.message.author.name.lower())['weaponatk']
		end = personas[str(endef)]['endurance']
	
	#Set minimum and maximum values.
	if int(strn) < 1:
		strn = 1
	if int(strn) > 99:
		strn = 99
		
	if int(atk) < 1:
		atk = 1
	if int(atk) > 999:
		atk = 999
	
	if int(end) < 1:
		end = 1
	if int(end) > 99:
		end = 99
		
	#Change the variables to floats.
	strn = float(strn)
	atk = float(atk)
	end = float(end)
	
	#Roll for random modifiers.
	roll = random.uniform(.94, 1.06)
	critroll = random.randrange(0, 25)
	
	#Damage formula.
	damage = (5.0 * sqrt((strn * atk)) / (((sqrt(end) * 1.25) / 2.0))) * roll
	
	if not name == "a":
		damage = damage / 4

	#Change the damage to an integer.
	damage = int(damage)
	
	#Set minimum and maximum damage.
	if damage < 0:
		damage = 0
	if damage > 5000:
		damage = 5000
		
	#Check for critical hit.
	if critroll == 1:
		#Change 'message' to reference the critical hit.
		message = "Critical hit! Total damage: "
			
		#Set critical modifier.
		damagemod = (sqrt(strn) / 3.5)
		
		#Set minimum and maximum critical modifier.
		if damagemod < 1.5:
			damagemod = 1.5
		if damagemod > 3:
			damagemod = 3
		
		#Apply critical modifier.
		damage = damage * damagemod
		
	#Set party gauge increase.
	if endef not in characterlist:
		partyGauge = partyGauge + (damage / 250)
		if partyGauge > 100:
			partyGauge = 100
	
	if not name == "a":
		eval(name)['currenthp'] -= damage
		if eval(name)['currenthp'] < 0:
			eval(name)['currenthp'] = 0
			message3 = str(eval(name)['firstname']) + " has fallen!"
	if name == "a":
		personas[str(endef)]['currenthp'] -= damage
		if personas[str(endef)]['currenthp'] < 0:
			personas[str(endef)]['currenthp'] = personas2[str(endef)]['hp']
			message3 = personas[str(endef)]['name'] + " has fallen!"
		
	#Tell bot to post damage.
	await bot.say(message + str(int(damage)) +"\nParty gauge: " + str(int(partyGauge)) + "%!\n" + message3)
	message = "Total damage: "
	message3 = ""
	
	#Print a confirmation message in the console.
	print("Attack confirmed. " + str(critroll))

@bot.command(name="skill", pass_context = True)
async def _skill(ctx, name, endef, name2="a"):
	global message
	global message2
	global message3
	global statusmessage
	global partyGauge
	
	if name2.lower() == "lucas":
		name2 = "joshkinz"
	if name2.lower() == "wes":
		name2 = "crying"
	if name2.lower() == "dorothy":
		name2 = "liminori"
	if name2.lower() == "limi":
		name2 = "liminori"
	if name2.lower() == "bailey":
		name2 = "swiggle"
	if name2.lower() == "ash":
		name2 = "shadowjoe323"
	if name2.lower() == "joe":
		name2 = "shadowjoe323"
	if name2.lower() == "shadowjoe":
		name2 = "shadowjoe323"
	if name2.lower() == "arlo":
		name2 = "lord_thantus"
	if name2.lower() == "thantus":
		name2 = "lord_thantus"
	if name2.lower() == "quentin":
		name2 = "qlonever"
	if name2.lower() == "qlon":
		name2 = "qlonever"
	if name2.lower() == "emily":
		name2 = "nintendofan"
	if name2.lower() == "nfan":
		name2 = "nintendofan"
		
	if endef.lower() == "lucas":
		endef = "joshkinz"
	if endef.lower() == "wes":
		endef = "crying"
	if endef.lower() == "dorothy":
		endef = "liminori"
	if endef.lower() == "limi":
		endef = "liminori"
	if endef.lower() == "bailey":
		endef = "swiggle"
	if endef.lower() == "ash":
		endef = "shadowjoe323"
	if endef.lower() == "joe":
		endef = "shadowjoe323"
	if endef.lower() == "shadowjoe":
		endef = "shadowjoe323"
	if endef.lower() == "arlo":
		endef = "lord_thantus"
	if endef.lower() == "thantus":
		endef = "lord_thantus"
	if endef.lower() == "quentin":
		endef = "qlonever"
	if endef.lower() == "qlon":
		endef = "qlonever"
	if endef.lower() == "emily":
		endef = "nintendofan"
	if endef.lower() == "nfan":
		endef = "nintendofan"
		
	if skills[str(name)]['type'] == "attack":	
		
		if name2 == "a":
			if not name in magiclist:
				strn = eval(ctx.message.author.name.lower())['strength']
			if name in magiclist:
				strn = eval(ctx.message.author.name.lower())['magic']
			atk = eval(ctx.message.author.name.lower())['weaponatk']
			end = personas[str(endef)]['endurance']
		if not name2 == "a":
			if not name in magiclist:
				strn = personas[str(endef)]['strength']
			if name in magiclist:
				strn = personas[str(endef)]['magic']
			atk = eval(name2)['weaponatk']
			end = eval(name2)['endurance']
			
		roll = random.uniform(.94, 1.06)
		roll = float(roll)
		roll2 = random.uniform(.94, 1.06)
		roll2 = float(roll2)
		critroll = random.randrange(0, skills[str(name)]['crit'])
		critroll2 = random.randrange(0, skills[str(name)]['crit'])
		statusroll = random.randrange(skills[str(name)]['status1'], skills[str(name)]['status2'])
		
		strn = float(strn)
		atk = float(atk)
		end = float(end)
		
		damage = (5.0 * sqrt((strn * atk)) / ((sqrt(end) * 1.25) / 2.0)) * float(roll) * float(skills[name]['strength'])
		damage2 = (5.0 * sqrt((strn * atk)) / ((sqrt(end) * 1.25) / 2.0)) * float(roll2) * float(skills[name]['strength'])
		
		if not name2 == "a":
			damage = damage / 4
			damage2 = damage2 / 4
			
		if name2 == "a":
			personas[str(endef)]['currenthp'] = personas[str(endef)]['currenthp'] - int(damage)
			if personas[str(endef)]['currenthp'] < 1:
				message3 = str(personas[str(endef)]['name']) + " has fallen!"
				personas[str(endef)]['currenthp'] = personas2[str(endef)]['hp']
		if not name2 == "a":
			eval(name2)['currenthp'] -= int(damage)
			personas[str(endef)]['currenthp'] -= int(damage)
			if personas[str(endef)]['currenthp'] < 1:
				message3 = str(personas[str(endef)]['name']) + " has fallen!"
				eval(name2)['currenthp'] = 0
				
		if name in magiclist:
			if ctx.message.author.name.lower() in characterlist:
				deduction = (skills[name]['cost2'])
				if deduction > eval(ctx.message.author.name.lower())['currentsp']:
					await bot.say("Not enough SP!")
					return
				else:	
					eval(ctx.message.author.name.lower())['currentsp'] = int(eval(ctx.message.author.name.lower())['currentsp']) - deduction
		if not name in magiclist:
			if ctx.message.author.name.lower() in characterlist:
				deduction = (eval(ctx.message.author.name.lower())['hp'] * skills[name]['cost2'])
				if deduction > eval(ctx.message.author.name.lower())['currenthp']:
					await bot.say("Not enough HP!")
					return
				else:	
					eval(ctx.message.author.name.lower())['currenthp'] = int(eval(ctx.message.author.name.lower())['currenthp']) - deduction
		if ctx.message.author.name.lower() in characterlist:
			eval(ctx.message.author.name.lower())['currenthp'] = int(eval(ctx.message.author.name.lower())['currenthp'])
			eval(ctx.message.author.name.lower())['currentsp'] = int(eval(ctx.message.author.name.lower())['currentsp'])
			
		if not name2 == "a":	
			if eval(name2)['currenthp'] < 1:
				eval(name2)['currenthp'] = 0
				message3 = str(eval(name2)['firstname']) + " has fallen!"
			if eval(name2)['currentsp'] < 1:
				eval(name2)['currentsp'] = 0
				
		damage = int(damage)
		damage2 = int(damage2)
		
		if damage < 0:
			damage = 0
		if damage > 5000:
			damage = 5000
		if damage2 < 0:
			damage2 = 0
		if damage2 > 5000:
			damage2 = 5000
			
		if critroll == 1:
			message = "Critical hit! Total damage: "
			
			damagemod = (sqrt(strn) / 3.5)
				
			if damagemod < 1.5:
				damagemod = 1.5
			if damagemod > 3:
				damagemod = 3
					
			damage = damage * damagemod
		
		if critroll2 == 1:
			message2 = "Critical hit! Total damage: "
			
			damagemod = (sqrt(strn) / 3.5)
				
			if damagemod < 1.5:
				damagemod = 1.5
			if damagemod > 3:
				damagemod = 3
					
			damage2 = damage2 * damagemod
		
		partyGauge = partyGauge + (sqrt(damage) / sqrt(end))
		if partyGauge > 100:
			partyGauge = 100
		
			
		if statusroll == 1:
			statusmessage = skills[str(name)]['status']
			
		if skills[str(name)]['hits'] == 2:
			await bot.say("Hit 1: " + message + str(int(damage)) + ".\nHit 2: " + message2 + str(int(damage2)) + ".\n" + message + str(int(damage + damage2)) + ".\nDeduct " + str(skills[str(name)]['cost']) + statusmessage + "\nParty gauge: " + str(int(partyGauge)) + "%!" + "\n" + message3)
			message3 = ""
		else:
			await bot.say(message + str(int(damage)) + ".\nDeduct " + str(skills[str(name)]['cost']) + ". " + statusmessage + "\nParty gauge: " + str(int(partyGauge)) + "%!" + "\n" + message3)
		message = "Total damage: "
		message2 = "Total damage: "
		message3 = ""
		statusmessage = ""
			
		print(str(skills[str(name)]['name']) + " confirmed! " + str(critroll) + " " + str(statusroll))
	
	if skills[str(name)]['type'] == 'buff':
		if ctx.message.author.name.lower() in characterlist:
				eval(ctx.message.author.name.lower())['currentsp'] = eval(ctx.message.author.name.lower())['currentsp'] - skills[name]['cost']
		partyGauge = int(partyGauge) + skills[str(name)]['gauge']
		await bot.say(skills[str(name)]['message'] + str(int(partyGauge)) + "%!\nDeduct " + str(skills[str(name)]['cost']) + " SP.")
		print("%s confirmed." % skills[str(name)]['name'])
		
	if skills[str(name)]['type'] == 'effect':
		statusroll = random.randrange(1, 3)
		if statusroll == 1:
			partyGauge = partyGauge + 1
			await bot.say(skills[str(name)]['message1'] + str(partyGauge) + "%!")
		else:
			await bot.say(skills[str(name)]['message2'] + "Deduct " + str(skills[str(name)]['cost']) + " SP.")
		print(skills[str(name)]['name'] + " confirmed. " + str(statusroll))
		
	if skills[str(name)]['type'] == 'heal':
		if not endef in characterlist:
			maxhp = personas[str(endef)]['hp']
			
		if endef in characterlist:
			maxhp = eval(endef)['hp']
			
		bonus = (maxhp / skills[str(name)]['bonus1'])
		
		hpgiven = bonus + skills[str(name)]['bonus2']
		hpgiven = int(hpgiven)
		
		if hpgiven > maxhp:
			hpgiven = maxhp
			
		partyGauge = partyGauge + (hpgiven / 110) + 3
		if int(partyGauge) > 100:
			partyGauge = 100
		
		eval(endef)['currenthp'] = eval(endef)['currenthp'] + hpgiven
		if eval(endef)['currenthp'] > eval(endef)['hp']:
			eval(endef)['currenthp'] = eval(endef)['hp']
			
		if ctx.message.author.name.lower() in characterlist:
				eval(ctx.message.author.name.lower())['currentsp'] = eval(ctx.message.author.name.lower())['currentsp'] - skills[name]['cost2']
		
		await bot.say("Restored " + str(hpgiven) + " HP!" +"\nDeduct " + str(skills[str(name)]['cost']) +".\nParty gauge: " + str(int(partyGauge)) + "%!")
		
		print("%s confirmed." % skills[str(name)]['name'])
		
	if skills[str(name)]['type'] == 'revive':
		hpgiven = eval(endef)['hp'] / int(skills[str(name)]['bonus'])
		partyGauge = partyGauge + skills[str(name)]['gauge']
		
		if ctx.message.author.name.lower() in characterlist:
			eval(ctx.message.author.name.lower())['currentsp'] = eval(ctx.message.author.name.lower())['currentsp'] - skills[name]['cost2']
		
		if name == "recarm":
			eval(endef)['currenthp'] = int(eval(endef)['hp'] / 2)
		if name == "samarecarm":
			eval(endef)['currenthp'] = int(eval(endef)['hp'])
		eval(endef)['currenthp'] = int(eval(endef)['currenthp'])
		await bot.say("Restored " + str(int(hpgiven)) + " HP! Deduct " + str(skills[str(name)]['cost'] + ".\nParty gauge: " + str(partyGauge) + "%!"))
		print(skills[str(name)]['name'] + " confirmed.")
		
@bot.command(name="party")
async def _partygauge(name):
	global partyGauge
	if name.lower() == "check":
		await bot.say("Party gauge: " + str(int(partyGauge)) + "%!")
		
		print("PG Check confirmed.")
	
	if name.lower() == "teamwork":
	
		if int(partyGauge) < 33:
			await bot.say("Not enough charge!\nParty gauge: " + str(int(partyGauge)) + "%!")
			
			print("Teamwork attack failed.")
		
		if int(partyGauge) > 32:
			partyGauge = int(partyGauge - 33)
			if int(partyGauge) < 0:
				partyGauge = 1
				
			await bot.say("Teamwork attack initiated!\nParty gauge: " + str(int(partyGauge)) + "%!")
			
			print("Teamwork Attack confirmed.")
			
	if name.lower() == "chain":
		if int(partyGauge) < 100:
			await bot.say("Not enough charge!\nParty gauge: " + str(int(partyGauge)) + "%!")
			print("Chain attack failed.")
			
		if int(partyGauge) > 99:
			partyGauge = int(partyGauge - 100)
			if int(partyGauge) < 0:
				partyGauge = 1
			await bot.say("Chain attack initiated!\nParty gauge: " + str(int(partyGauge)) + "%!")
			print("Chain Attack confirmed.")
					
@bot.command(name="gauge", pass_context = True)
async def _gauge(ctx, name, number):
	global partyGauge
	if ctx.message.author.server_permissions.administrator:
		if name.lower() == "increase":
			partyGauge = partyGauge + int(number)
			if int(partyGauge) < 0:
				partyGauge = 1
			if int(partyGauge) > 100:
					partyGauge = 100
			await bot.say("Party gauge: " + str(partyGauge) + "%!")
			print("Party gauge increased by " + str(number) + "%")
			
		if name.lower() == "decrease":
			partyGauge = partyGauge - int(number)
			if int(partyGauge) < 0:
				partyGauge = 1
			if int(partyGauge) > 100:
					partyGauge = 100
			await bot.say("Party gauge: " + str(partyGauge) + "%!")
			print("Party gauge decreased by " + str(number) + "%")
	else:
		await bot.say("This command is only usable by administrators.")
		print("Invalid gauge command by " + ctx.message.author.name)
		
@bot.command(name="status", pass_context = True)
async def _status(ctx, name='a'):
	if name.lower() == "lucas":
		name = "joshkinz"
	if name.lower() == "wes":
		name = "crying"
	if name.lower() == "dorothy":
		name = "liminori"
	if name.lower() == "limi":
		name = "liminori"
	if name.lower() == "bailey":
		name = "swiggle"
	if name.lower() == "ash":
		name = "shadowjoe323"
	if name.lower() == "joe":
		name = "shadowjoe323"
	if name.lower() == "shadowjoe":
		name = "shadowjoe323"
	if name.lower() == "arlo":
		name = "lord_thantus"
	if name.lower() == "thantus":
		name = "lord_thantus"
	if name.lower() == "quentin":
		name = "qlonever"
	if name.lower() == "qlon":
		name = "qlonever"
	if name.lower() == "emily":
		name = "nintendofan"
	if name.lower() == "nfan":
		name = "nintendofan"
		
	character = eval(ctx.message.author.name.lower())
	if not name == 'a':
		character2 = eval(ctx.message.author.name.lower())
		persona2 = eval(ctx.message.author.name.lower())['persona']
	persona = character['persona']
	
	if name == 'a':
		await bot.say("**STATUS**\n----------\n")
		await bot.say("Name: " + character['firstname'] + " " + character['lastname'] + "\nTeam: " + character['team'] + "\nClass: " + character['class'] + "\nHP: " + str(character['hp']) + "\nSP: " + str(character['sp']) + "\nStrength: " + str(character['strength']) + "\nMagic: " + str(character['magic']) + "\nEndurance: " + str(character['endurance']) + "\nWeapon ATK: " + str(character['weaponatk']) + "\nLevel: " + str(character['level']) + "\nXP to Next: " + str(character['xp']))
		await bot.say("**PERSONAS**\n----------")
		if not persona['persona1']['name'] == "n/a":
			await bot.say("Name 1: " + persona['persona1']['name'] + "\nClass: " + persona['persona1']['class'] + "\nSkill 1: " + persona['persona1']['skill1'] + "\nSkill 2: " + persona['persona1']['skill2'] + "\nSkill 3: " + persona['persona1']['skill3'] + "\nSkill 4: " + persona['persona1']['skill4'])
		if not persona['persona2']['name'] == "n/a":
			await bot.say("Name 2: " + persona['persona2']['name'] + "\nClass: " + persona['persona2']['class'] + "\nSkill 1: " + persona['persona2']['skill1'] + "\nSkill 2: " + persona['persona2']['skill2'] + "\nSkill 3: " + persona['persona2']['skill3'] + "\nSkill 4: " + persona['persona2']['skill4'])
		if not persona['persona3']['name'] == "n/a":
			await bot.say("Name 3: " + persona['persona3']['name'] + "\nClass: " + persona['persona3']['class'] + "\nSkill 1: " + persona['persona3']['skill1'] + "\nSkill 2: " + persona['persona3']['skill2'] + "\nSkill 3: " + persona['persona3']['skill3'] + "\nSkill 4: " + persona['persona3']['skill4'])
		if not persona['persona4']['name'] == "n/a":
			await bot.say("Name 4: " + persona['persona4']['name'] + "\nClass: " + persona['persona4']['class'] + "\nSkill 1: " + persona['persona4']['skill1'] + "\nSkill 2: " + persona['persona4']['skill2'] + "\nSkill 3: " + persona['persona4']['skill3'] + "\nSkill 4: " + persona['persona4']['skill4'])
	else:
		await bot.say("**STATUS**\n----------\n")
		await bot.say("Name: " + character2['firstname'] + " " + character2['lastname'] + "\nTeam: " + character2['team'] + "\nClass: " + character2['class'] + "\nHP: " + str(character2['hp']) + "\nSP: " + str(character2['sp']) + "\nWeapon ATK: " + str(character2['weaponatk']) + "\nLevel: " + str(character2['level']) + "\nXP to Next: " + str(character2['xp']))
		await bot.say("**PERSONAS**\n----------")
		if not persona['persona1']['name'] == "n/a":
			await bot.say("Name 1: " + persona2['persona1']['name'] + "\nClass: " + persona2['persona1']['class'] + "\nSkill 1: " + persona2['persona1']['skill1'] + "\nSkill 2: " + persona2['persona1']['skill2'] + "\nSkill 3: " + persona2['persona1']['skill3'] + "\nSkill 4: " + persona2['persona1']['skill4'])
		if not persona['persona2']['name'] == "n/a":
			await bot.say("Name 2: " + persona2['persona2']['name'] + "\nClass: " + persona2['persona2']['class'] + "\nSkill 1: " + persona2['persona2']['skill1'] + "\nSkill 2: " + persona2['persona2']['skill2'] + "\nSkill 3: " + persona2['persona2']['skill3'] + "\nSkill 4: " + persona2['persona2']['skill4'])
		if not persona['persona3']['name'] == "n/a":
			await bot.say("Name 3: " + persona2['persona3']['name'] + "\nClass: " + persona2['persona3']['class'] + "\nSkill 1: " + persona2['persona3']['skill1'] + "\nSkill 2: " + persona2['persona3']['skill2'] + "\nSkill 3: " + persona2['persona3']['skill3'] + "\nSkill 4: " + persona2['persona3']['skill4'])
		if not persona['persona4']['name'] == "n/a":
			await bot.say("Name 4: " + persona2['persona4']['name'] + "\nClass: " + persona2['persona4']['class'] + "\nSkill 1: " + persona2['persona4']['skill1'] + "\nSkill 2: " + persona2['persona4']['skill2'] + "\nSkill 3: " + persona2['persona4']['skill3'] + "\nSkill 4: " + persona2['persona4']['skill4'])

@bot.command(name="levelup", pass_context = True)
async def _levelup(ctx, name):
	if name.lower() == "lucas":
		name = "joshkinz"
	if name.lower() == "wes":
		name = "crying"
	if name.lower() == "dorothy":
		name = "liminori"
	if name.lower() == "limi":
		name = "liminori"
	if name.lower() == "bailey":
		name = "swiggle"
	if name.lower() == "ash":
		name = "shadowjoe323"
	if name.lower() == "joe":
		name = "shadowjoe323"
	if name.lower() == "shadowjoe":
		name = "shadowjoe323"
	if name.lower() == "arlo":
		name = "lord_thantus"
	if name.lower() == "thantus":
		name = "lord_thantus"
	if name.lower() == "quentin":
		name = "qlonever"
	if name.lower() == "qlon":
		name = "qlonever"
	if name.lower() == "emily":
		name = "nintendofan"
	if name.lower() == "nfan":
		name = "nintendofan"
		
	strength = eval(name)['strength']
	magic = eval(name)['magic']
	endurance = eval(name)['endurance']
		
	if ctx.message.author.server_permissions.administrator:
		eval(name)['level'] = eval(name)['level'] + 1
		eval(name)['xp'] = xpcurve[str(eval(name)['level'])]['xp']
		
		hproll = random.randrange(7, 15)
		sproll = random.randrange(4, 9)
		eval(name)['hp'] = eval(name)['hp'] + hproll
		eval(name)['sp'] = eval(name)['sp'] + sproll
		
		if eval(name)['boon'] == 'str':
			if eval(name)['bane'] == 'mag':
				levelup = ['Strength', 'Strength', 'Strength', 'Endurance', 'Endurance', 'Magic']
				levelup1 = random.choice(levelup)
				levelup2 = random.choice(levelup)
			if eval(name)['bane'] == 'end':
				levelup = ['Strength', 'Strength', 'Strength', 'Endurance', 'Magic', 'Magic']
				levelup1 = random.choice(levelup)
				levelup2 = random.choice(levelup)
		if eval(name)['boon'] == 'mag':
			if eval(name)['bane'] == 'str':
				levelup = ['Strength', 'Endurance', 'Endurance', 'Magic', 'Magic', 'Magic']
				levelup1 = random.choice(levelup)
				levelup2 = random.choice(levelup)
			if eval(name)['bane'] == 'end':
				levelup = ['Strength', 'Strength', 'Endurance', 'Magic', 'Magic', 'Magic']
				levelup1 = random.choice(levelup)
				levelup2 = random.choice(levelup)
		if eval(name)['boon'] == 'end':
			if eval(name)['bane'] == 'str':
				levelup = ['Strength', 'Endurance', 'Endurance', 'Endurance', 'Magic', 'Magic']
				levelup1 = random.choice(levelup)
				levelup2 = random.choice(levelup)
			if eval(name)['bane'] == 'mag':
				levelup = ['Strength', 'Strength', 'Endurance', 'Endurance', 'Endurance', 'Magic']
				levelup1 = random.choice(levelup)
				levelup2 = random.choice(levelup)
		await bot.say("Level up! Level " + str(eval(name)['level']) + "\nStats increased: " + levelup1 + " and " + levelup2 + "\nHp: " + str(eval(name)['hp']) + "\nSP: " + str(eval(name)['sp']))
		if levelup1 == 'Strength':
			if levelup2 == 'Strength':
				strength = eval(name)['strength'] + 2
			if levelup2 == 'Magic':
				strength = eval(name)['strength'] + 1
				magic = eval(name)['magic'] + 1
			if levelup2 == 'Endurance':
				strength = eval(name)['strength'] + 1
				endurance = eval(name)['endurance'] + 1
		if levelup1 == 'Magic':
			if levelup2 == 'Strength':
				magic = eval(name)['magic'] + 1
				strength = eval(name)['strength'] + 1
			if levelup2 == 'Magic':
				magic = eval(name)['magic'] + 2
			if levelup2 == 'Endurance':
				magic = eval(name)['magic'] + 1
				endurance = eval(name)['endurance'] + 1
		if levelup1 == 'Endurance':
			if levelup2 == 'Strength':
				endurance = eval(name)['endurance'] + 1
				strength = eval(name)['strength'] + 1
			if levelup2 == 'Magic':
				endurance = eval(name)['endurance'] + 1
				magic = eval(name)['magic'] + 1
			if levelup2 == 'Endurance':
				endurance = eval(name)['endurance'] + 2
		
		data = {
		"firstname": eval(name)['firstname'],
		"lastname": eval(name)['lastname'],
		"class": eval(name)['class'],
		"persona": {
			"persona1": {
				"name": eval(name)['persona']['persona1']['name'],
				"class": eval(name)['persona']['persona1']['class'],
				"skill1": eval(name)['persona']['persona1']['skill1'],
				"skill2": eval(name)['persona']['persona1']['skill2'],
				"skill3": eval(name)['persona']['persona1']['skill3'],
				"skill4": eval(name)['persona']['persona1']['skill4']
			},
			"persona2": {
				"name": eval(name)['persona']['persona2']['name'],
				"class": eval(name)['persona']['persona2']['class'],
				"skill1": eval(name)['persona']['persona2']['skill1'],
				"skill2": eval(name)['persona']['persona2']['skill2'],
				"skill3": eval(name)['persona']['persona2']['skill3'],
				"skill4": eval(name)['persona']['persona2']['skill4']
			},
			"persona3": {
				"name": eval(name)['persona']['persona3']['name'],
				"class": eval(name)['persona']['persona3']['class'],
				"skill1": eval(name)['persona']['persona3']['skill1'],
				"skill2": eval(name)['persona']['persona3']['skill2'],
				"skill3": eval(name)['persona']['persona3']['skill3'],
				"skill4": eval(name)['persona']['persona3']['skill4']
			},
			"persona4": {
				"name": eval(name)['persona']['persona4']['class'],
				"class": eval(name)['persona']['persona4']['name'],
				"skill1": eval(name)['persona']['persona4']['skill1'],
				"skill2": eval(name)['persona']['persona4']['skill2'],
				"skill3": eval(name)['persona']['persona4']['skill3'],
				"skill4": eval(name)['persona']['persona4']['skill4']
			}
		},
		"boon": eval(name)['boon'],
		"bane": eval(name)['bane'],
		"team": eval(name)['team'],
		"level": eval(name)['level'],
		"xp": eval(name)['xp'],
		"strength": strength,
		"magic": magic,
		"endurance": endurance,
		"weaponatk": eval(name)['weaponatk'],
		"hp": eval(name)['hp'],
		"currenthp": eval(name)['currenthp'],
		"sp": eval(name)['sp'],
		"currentsp": eval(name)['currentsp']
	}
		d = json.dumps(data)
		with open("characters/" + str(name) + ".json","w") as f:
			f.write(d)
			
@bot.command(name="weapon", pass_context = True)
async def _weapon(ctx, value):
	eval(ctx.message.author.name.lower())['weaponatk'] = value
	await bot.say("Successfully updated weapon!")
	data = {
		"firstname": eval(ctx.message.author.name.lower())['firstname'],
		"lastname": eval(ctx.message.author.name.lower())['lastname'],
		"class": eval(ctx.message.author.name.lower())['class'],
		"persona": {
			"persona1": {
				"name": eval(ctx.message.author.name.lower())['persona']['persona1']['name'],
				"class": eval(ctx.message.author.name.lower())['persona']['persona1']['class'],
				"skill1": eval(ctx.message.author.name.lower())['persona']['persona1']['skill1'],
				"skill2": eval(ctx.message.author.name.lower())['persona']['persona1']['skill2'],
				"skill3": eval(ctx.message.author.name.lower())['persona']['persona1']['skill3'],
				"skill4": eval(ctx.message.author.name.lower())['persona']['persona1']['skill4']
			},
			"persona2": {
				"name": eval(ctx.message.author.name.lower())['persona']['persona2']['name'],
				"class": eval(ctx.message.author.name.lower())['persona']['persona2']['class'],
				"skill1": eval(ctx.message.author.name.lower())['persona']['persona2']['skill1'],
				"skill2": eval(ctx.message.author.name.lower())['persona']['persona2']['skill2'],
				"skill3": eval(ctx.message.author.name.lower())['persona']['persona2']['skill3'],
				"skill4": eval(ctx.message.author.name.lower())['persona']['persona2']['skill4']
			},
			"persona3": {
				"name": eval(ctx.message.author.name.lower())['persona']['persona3']['name'],
				"class": eval(ctx.message.author.name.lower())['persona']['persona3']['class'],
				"skill1": eval(ctx.message.author.name.lower())['persona']['persona3']['skill1'],
				"skill2": eval(ctx.message.author.name.lower())['persona']['persona3']['skill2'],
				"skill3": eval(ctx.message.author.name.lower())['persona']['persona3']['skill3'],
				"skill4": eval(ctx.message.author.name.lower())['persona']['persona3']['skill4']
			},
			"persona4": {
				"name": eval(ctx.message.author.name.lower())['persona']['persona4']['class'],
				"class": eval(ctx.message.author.name.lower())['persona']['persona4']['name'],
				"skill1": eval(ctx.message.author.name.lower())['persona']['persona4']['skill1'],
				"skill2": eval(ctx.message.author.name.lower())['persona']['persona4']['skill2'],
				"skill3": eval(ctx.message.author.name.lower())['persona']['persona4']['skill3'],
				"skill4": eval(ctx.message.author.name.lower())['persona']['persona4']['skill4']
			}
		},
		"boon":eval(ctx.message.author.name.lower())['boon'],
		"bane": eval(ctx.message.author.name.lower())['bane'],
		"team": eval(ctx.message.author.name.lower())['team'],
		"level": eval(ctx.message.author.name.lower())['level'],
		"xp": eval(ctx.message.author.name.lower())['xp'],
		"strength": eval(ctx.message.author.name.lower())['strength'],
		"magic": eval(ctx.message.author.name.lower())['magic'],
		"endurance": eval(ctx.message.author.name.lower())['endurance'],
		"weaponatk": int(value),
		"hp": eval(ctx.message.author.name.lower())['hp'],
		"sp": eval(ctx.message.author.name.lower())['sp'],
	}
	d = json.dumps(data)
	with open("characters/" + str(ctx.message.author.name.lower()) + ".json","w") as f:
		f.write(d)
	
@bot.command(name="check", pass_context = True)
async def _check(ctx):
	if eval(ctx.message.author.name.lower())['team'] == "Law Team":
		await bot.say("Lucas: " + str(joshkinz['currenthp']) + "/" + str(joshkinz['hp']) + " HP, " + str(joshkinz['currentsp']) + "/" + str(joshkinz['sp']) + " SP\nWes: " + str(crying['currenthp']) + "/" + str(crying['hp']) + " HP, " + str(crying['currentsp']) + "/" + str(crying['sp']) + " SP\nDorothy: " + str(liminori['currenthp']) + "/" + str(liminori['hp']) + " HP, " + str(liminori['currentsp']) + "/" + str(liminori['sp']) + " SP\nBailey: " + str(swiggle['currenthp']) + "/" + str(swiggle['hp']) + " HP, " + str(swiggle['currentsp']) + "/" + str(swiggle['sp']) + " SP")
	if eval(ctx.message.author.name.lower())['team'] == "Chaos Team":
		await bot.say("Ash: " + str(shadowjoe323['currenthp']) + "/" + str(shadowjoe323['hp']) + " HP, " + str(shadowjoe323['currentsp']) + "/" + str(shadowjoe323['sp']) + " SP\nQuentin: " + str(qlonever['currenthp']) + "/" + str(qlonever['hp']) + " HP, " + str(qlonever['currentsp']) + "/" + str(qlonever['sp']) + " SP\nArlo: " + str(lord_thantus['currenthp']) + "/" + str(lord_thantus['hp']) + " HP, " + str(lord_thantus['currentsp']) + "/" + str(lord_thantus['sp']) + " SP\nEmily: " + str(nintendofan['currenthp']) + "/" + str(nintendofan['hp']) + " HP, " + str(nintendofan['currentsp']) + "/" + str(nintendofan['sp']) + " SP")

@bot.command(name="persona", pass_context = True)
async def _persona(ctx, command, number, personaname, name='a'):
	name = name.lower()
	if name.lower() == "lucas":
		name = "joshkinz"
	if name.lower() == "wes":
		name = "crying"
	if name.lower() == "dorothy":
		name = "liminori"
	if name.lower() == "limi":
		name = "liminori"
	if name.lower() == "bailey":
		name = "swiggle"
	if name.lower() == "ash":
		name = "shadowjoe323"
	if name.lower() == "joe":
		name = "shadowjoe323"
	if name.lower() == "shadowjoe":
		name = "shadowjoe323"
	if name.lower() == "arlo":
		name = "lord_thantus"
	if name.lower() == "thantus":
		name = "lord_thantus"
	if name.lower() == "quentin":
		name = "qlonever"
	if name.lower() == "qlon":
		name = "qlonever"
	if name.lower() == "emily":
		name = "nintendofan"
	if name.lower() == "nfan":
		name = "nintendofan"
	if ctx.message.author.server_permissions.administrator:
		if command == "add":
			print("confirmed")
			if int(number) == 1:
				eval(name)['persona']['persona1']['name'] = personas[str(personaname)]['name']
				eval(name)['persona']['persona1']['class'] = personas[str(personaname)]['class']
				eval(name)['persona']['persona1']['skill1'] = personas[str(personaname)]['skill1']
				eval(name)['persona']['persona1']['skill2'] = personas[str(personaname)]['skill2']
				eval(name)['persona']['persona1']['skill3'] = personas[str(personaname)]['skill3']
				eval(name)['persona']['persona1']['skill4'] = personas[str(personaname)]['skill4']
				data = {
					"firstname": eval(name)['firstname'],
					"lastname": eval(name)['lastname'],
					"class": eval(name)['class'],
					"persona": {
						"persona1": {
							"name": personas[str(personaname)]['name'],
							"class": personas[str(personaname)]['class'],
							"skill1": personas[str(personaname)]['skill1'],
							"skill2": personas[str(personaname)]['skill2'],
							"skill3": personas[str(personaname)]['skill3'],
							"skill4": personas[str(personaname)]['skill4']
						},
						"persona2": {
							"name": eval(name)['persona']['persona2']['name'],
							"class": eval(name)['persona']['persona2']['class'],
							"skill1": eval(name)['persona']['persona2']['skill1'],
							"skill2": eval(name)['persona']['persona2']['skill2'],
							"skill3": eval(name)['persona']['persona2']['skill3'],
							"skill4": eval(name)['persona']['persona2']['skill4']
						},
						"persona3": {
							"name": eval(name)['persona']['persona3']['name'],
							"class": eval(name)['persona']['persona3']['class'],
							"skill1": eval(name)['persona']['persona3']['skill1'],
							"skill2": eval(name)['persona']['persona3']['skill2'],
							"skill3": eval(name)['persona']['persona3']['skill3'],
							"skill4": eval(name)['persona']['persona3']['skill4']
						},
						"persona4": {
							"name": eval(name)['persona']['persona4']['class'],
							"class": eval(name)['persona']['persona4']['name'],
							"skill1": eval(name)['persona']['persona4']['skill1'],
							"skill2": eval(name)['persona']['persona4']['skill2'],
							"skill3": eval(name)['persona']['persona4']['skill3'],
							"skill4": eval(name)['persona']['persona4']['skill4']
						}
					},
					"boon": eval(name)['boon'],
					"bane": eval(name)['bane'],
					"team": eval(name)['team'],
					"level": eval(name)['level'],
					"xp": eval(name)['xp'],
					"strength": eval(name)['strength'],
					"magic": eval(name)['magic'],
					"endurance": eval(name)['endurance'],
					"weaponatk": eval(name)['weaponatk'],
					"hp": eval(name)['hp'],
					"currenthp": eval(name)['currenthp'],
					"sp": eval(name)['sp'],
					"currentsp": eval(name)['currentsp']
				}
				d = json.dumps(data)
				with open("characters/" + str(name) + ".json","w") as f:
					f.write(d)
					
			if int(number) == 2:
				eval(name)['persona']['persona2']['name'] = personas[str(personaname)]['name']
				eval(name)['persona']['persona2']['class'] = personas[str(personaname)]['class']
				eval(name)['persona']['persona2']['skill1'] = personas[str(personaname)]['skill1']
				eval(name)['persona']['persona2']['skill2'] = personas[str(personaname)]['skill2']
				eval(name)['persona']['persona2']['skill3'] = personas[str(personaname)]['skill3']
				eval(name)['persona']['persona2']['skill4'] = personas[str(personaname)]['skill4']
				data = {
					"firstname": eval(name)['firstname'],
					"lastname": eval(name)['lastname'],
					"class": eval(name)['class'],
					"persona": {
						"persona1": {
							"name": eval(name)['persona']['persona1']['name'],
							"class": eval(name)['persona']['persona1']['class'],
							"skill1": eval(name)['persona']['persona1']['skill1'],
							"skill2": eval(name)['persona']['persona1']['skill2'],
							"skill3": eval(name)['persona']['persona1']['skill3'],
							"skill4": eval(name)['persona']['persona1']['skill4']
						},
						"persona2": {
							"name": personas[str(personaname)]['name'],
							"class": personas[str(personaname)]['class'],
							"skill1": personas[str(personaname)]['skill1'],
							"skill2": personas[str(personaname)]['skill2'],
							"skill3": personas[str(personaname)]['skill3'],
							"skill4": personas[str(personaname)]['skill4']
						},
						"persona3": {
							"name": eval(name)['persona']['persona3']['name'],
							"class": eval(name)['persona']['persona3']['class'],
							"skill1": eval(name)['persona']['persona3']['skill1'],
							"skill2": eval(name)['persona']['persona3']['skill2'],
							"skill3": eval(name)['persona']['persona3']['skill3'],
							"skill4": eval(name)['persona']['persona3']['skill4']
						},
						"persona4": {
							"name": eval(name)['persona']['persona4']['class'],
							"class": eval(name)['persona']['persona4']['name'],
							"skill1": eval(name)['persona']['persona4']['skill1'],
							"skill2": eval(name)['persona']['persona4']['skill2'],
							"skill3": eval(name)['persona']['persona4']['skill3'],
							"skill4": eval(name)['persona']['persona4']['skill4']
						}
					},
					"boon": eval(name)['boon'],
					"bane": eval(name)['bane'],
					"team": eval(name)['team'],
					"level": eval(name)['level'],
					"xp": eval(name)['xp'],
					"strength": eval(name)['strength'],
					"magic": eval(name)['magic'],
					"endurance": eval(name)['endurance'],
					"weaponatk": eval(name)['weaponatk'],
					"hp": eval(name)['hp'],
					"currenthp": eval(name)['currenthp'],
					"sp": eval(name)['sp'],
					"currentsp": eval(name)['currentsp']
				}
				d = json.dumps(data)
				with open("characters/" + str(name) + ".json","w") as f:
					f.write(d)
					
			if int(number) == 3:
				eval(name)['persona']['persona3']['name'] = personas[str(personaname)]['name']
				eval(name)['persona']['persona3']['class'] = personas[str(personaname)]['class']
				eval(name)['persona']['persona3']['skill1'] = personas[str(personaname)]['skill1']
				eval(name)['persona']['persona3']['skill2'] = personas[str(personaname)]['skill2']
				eval(name)['persona']['persona3']['skill3'] = personas[str(personaname)]['skill3']
				eval(name)['persona']['persona3']['skill4'] = personas[str(personaname)]['skill4']
				data = {
					"firstname": eval(name)['firstname'],
					"lastname": eval(name)['lastname'],
					"class": eval(name)['class'],
					"persona": {
						"persona1": {
							"name": eval(name)['persona']['persona1']['name'],
							"class": eval(name)['persona']['persona1']['class'],
							"skill1": eval(name)['persona']['persona1']['skill1'],
							"skill2": eval(name)['persona']['persona1']['skill2'],
							"skill3": eval(name)['persona']['persona1']['skill3'],
							"skill4": eval(name)['persona']['persona1']['skill4']
						},
						"persona2": {
							"name": eval(name)['persona']['persona2']['name'],
							"class": eval(name)['persona']['persona2']['class'],
							"skill1": eval(name)['persona']['persona2']['skill1'],
							"skill2": eval(name)['persona']['persona2']['skill2'],
							"skill3": eval(name)['persona']['persona2']['skill3'],
							"skill4": eval(name)['persona']['persona2']['skill4']
						},
						"persona3": {
							"name": personas[str(personaname)]['name'],
							"class": personas[str(personaname)]['class'],
							"skill1": personas[str(personaname)]['skill1'],
							"skill2": personas[str(personaname)]['skill2'],
							"skill3": personas[str(personaname)]['skill3'],
							"skill4": personas[str(personaname)]['skill4']
						},
						"persona4": {
							"name": eval(name)['persona']['persona4']['class'],
							"class": eval(name)['persona']['persona4']['name'],
							"skill1": eval(name)['persona']['persona4']['skill1'],
							"skill2": eval(name)['persona']['persona4']['skill2'],
							"skill3": eval(name)['persona']['persona4']['skill3'],
							"skill4": eval(name)['persona']['persona4']['skill4']
						}
					},
					"boon": eval(name)['boon'],
					"bane": eval(name)['bane'],
					"team": eval(name)['team'],
					"level": eval(name)['level'],
					"xp": eval(name)['xp'],
					"strength": eval(name)['strength'],
					"magic": eval(name)['magic'],
					"endurance": eval(name)['endurance'],
					"weaponatk": eval(name)['weaponatk'],
					"hp": eval(name)['hp'],
					"currenthp": eval(name)['currenthp'],
					"sp": eval(name)['sp'],
					"currentsp": eval(name)['currentsp']
				}
				d = json.dumps(data)
				with open("characters/" + str(name) + ".json","w") as f:
					f.write(d)
			
			if int(number) == 4:
				eval(name)['persona']['persona4']['name'] = personas[str(personaname)]['name']
				eval(name)['persona']['persona4']['class'] = personas[str(personaname)]['class']
				eval(name)['persona']['persona4']['skill1'] = personas[str(personaname)]['skill1']
				eval(name)['persona']['persona4']['skill2'] = personas[str(personaname)]['skill2']
				eval(name)['persona']['persona4']['skill3'] = personas[str(personaname)]['skill3']
				eval(name)['persona']['persona4']['skill4'] = personas[str(personaname)]['skill4']
				data = {
					"firstname": eval(name)['firstname'],
					"lastname": eval(name)['lastname'],
					"class": eval(name)['class'],
					"persona": {
						"persona1": {
							"name": eval(name)['persona']['persona1']['name'],
							"class": eval(name)['persona']['persona1']['class'],
							"skill1": eval(name)['persona']['persona1']['skill1'],
							"skill2": eval(name)['persona']['persona1']['skill2'],
							"skill3": eval(name)['persona']['persona1']['skill3'],
							"skill4": eval(name)['persona']['persona1']['skill4']
						},
						"persona2": {
							"name": eval(name)['persona']['persona2']['name'],
							"class": eval(name)['persona']['persona2']['class'],
							"skill1": eval(name)['persona']['persona2']['skill1'],
							"skill2": eval(name)['persona']['persona2']['skill2'],
							"skill3": eval(name)['persona']['persona2']['skill3'],
							"skill4": eval(name)['persona']['persona2']['skill4']
						},
						"persona3": {
							"name": eval(name)['persona']['persona3']['name'],
							"class": eval(name)['persona']['persona3']['class'],
							"skill1": eval(name)['persona']['persona3']['skill1'],
							"skill2": eval(name)['persona']['persona3']['skill2'],
							"skill3": eval(name)['persona']['persona3']['skill3'],
							"skill4": eval(name)['persona']['persona3']['skill4']
						},
						"persona4": {
							"name": personas[str(personaname)]['name'],
							"class": personas[str(personaname)]['class'],
							"skill1": personas[str(personaname)]['skill1'],
							"skill2": personas[str(personaname)]['skill2'],
							"skill3": personas[str(personaname)]['skill3'],
							"skill4": personas[str(personaname)]['skill4']
						}
					},
					"boon": eval(name)['boon'],
					"bane": eval(name)['bane'],
					"team": eval(name)['team'],
					"level": eval(name)['level'],
					"xp": eval(name)['xp'],
					"strength": eval(name)['strength'],
					"magic": eval(name)['magic'],
					"endurance": eval(name)['endurance'],
					"weaponatk": eval(name)['weaponatk'],
					"hp": eval(name)['hp'],
					"currenthp": eval(name)['currenthp'],
					"sp": eval(name)['sp'],
					"currentsp": eval(name)['currentsp']
				}
				d = json.dumps(data)
				with open("characters/" + str(name) + ".json","w") as f:
					f.write(d)
				
		if command == "remove":
			if int(number) == 1:
				eval(personaname)['persona']['persona1']['name'] = "n/a"
				eval(personaname)['persona']['persona1']['class'] = "n/a"
				eval(personaname)['persona']['persona1']['skill1'] = "n/a"
				eval(personaname)['persona']['persona1']['skill2'] = "n/a"
				eval(personaname)['persona']['persona1']['skill3'] = "n/a"
				eval(personaname)['persona']['persona1']['skill4'] = "n/a"
				data = {
					"firstname": eval(personaname)['firstname'],
					"lastname": eval(personaname)['lastname'],
					"class": eval(personaname)['class'],
					"persona": {
						"persona1": {
							"name": "n/a",
							"class": "n/a",
							"skill1": "n/a",
							"skill2": "n/a",
							"skill3": "n/a",
							"skill4": "n/a"
						},
						"persona2": {
							"name": eval(personaname)['persona']['persona2']['name'],
							"class": eval(personaname)['persona']['persona2']['class'],
							"skill1": eval(personaname)['persona']['persona2']['skill1'],
							"skill2": eval(personaname)['persona']['persona2']['skill2'],
							"skill3": eval(personaname)['persona']['persona2']['skill3'],
							"skill4": eval(personaname)['persona']['persona2']['skill4']
						},
						"persona3": {
							"name": eval(personaname)['persona']['persona3']['name'],
							"class": eval(personaname)['persona']['persona3']['class'],
							"skill1": eval(personaname)['persona']['persona3']['skill1'],
							"skill2": eval(personaname)['persona']['persona3']['skill2'],
							"skill3": eval(personaname)['persona']['persona3']['skill3'],
							"skill4": eval(personaname)['persona']['persona3']['skill4']
						},
						"persona4": {
							"name": eval(personaname)['persona']['persona4']['class'],
							"class": eval(personaname)['persona']['persona4']['name'],
							"skill1": eval(personaname)['persona']['persona4']['skill1'],
							"skill2": eval(personaname)['persona']['persona4']['skill2'],
							"skill3": eval(personaname)['persona']['persona4']['skill3'],
							"skill4": eval(personaname)['persona']['persona4']['skill4']
						}
					},
					"boon": eval(personaname)['boon'],
					"bane": eval(personaname)['bane'],
					"team": eval(personaname)['team'],
					"level": eval(personaname)['level'],
					"xp": eval(personaname)['xp'],
					"strength": eval(personaname)['strength'],
					"magic": eval(personaname)['magic'],
					"endurance": eval(personaname)['endurance'],
					"weaponatk": eval(personaname)['weaponatk'],
					"hp": eval(personaname)['hp'],
					"currenthp": eval(personaname)['currenthp'],
					"sp": eval(personaname)['sp'],
					"currentsp": eval(personaname)['currentsp']
				}
				d = json.dumps(data)
				with open("characters/" + str(personaname) + ".json","w") as f:
					f.write(d)
					
			if int(number) == 2:
				eval(personaname)['persona']['persona2']['name'] = "n/a"
				eval(personaname)['persona']['persona2']['class'] = "n/a"
				eval(personaname)['persona']['persona2']['skill1'] = "n/a"
				eval(personaname)['persona']['persona2']['skill2'] = "n/a"
				eval(personaname)['persona']['persona2']['skill3'] = "n/a"
				eval(personaname)['persona']['persona2']['skill4'] = "n/a"
				data = {
					"firstname": eval(personaname)['firstname'],
					"lastname": eval(personaname)['lastname'],
					"class": eval(personaname)['class'],
					"persona": {
						"persona1": {
							"name": eval(personaname)['persona']['persona1']['name'],
							"class": eval(personaname)['persona']['persona1']['class'],
							"skill1": eval(personaname)['persona']['persona1']['skill1'],
							"skill2": eval(personaname)['persona']['persona1']['skill2'],
							"skill3": eval(personaname)['persona']['persona1']['skill3'],
							"skill4": eval(personaname)['persona']['persona1']['skill4']
						},
						"persona2": {
							"name": "n/a",
							"class": "n/a",
							"skill1": "n/a",
							"skill2": "n/a",
							"skill3": "n/a",
							"skill4": "n/a"
						},
						"persona3": {
							"name": eval(personaname)['persona']['persona3']['name'],
							"class": eval(personaname)['persona']['persona3']['class'],
							"skill1": eval(personaname)['persona']['persona3']['skill1'],
							"skill2": eval(personaname)['persona']['persona3']['skill2'],
							"skill3": eval(personaname)['persona']['persona3']['skill3'],
							"skill4": eval(personaname)['persona']['persona3']['skill4']
						},
						"persona4": {
							"name": eval(personaname)['persona']['persona4']['class'],
							"class": eval(personaname)['persona']['persona4']['name'],
							"skill1": eval(personaname)['persona']['persona4']['skill1'],
							"skill2": eval(personaname)['persona']['persona4']['skill2'],
							"skill3": eval(personaname)['persona']['persona4']['skill3'],
							"skill4": eval(personaname)['persona']['persona4']['skill4']
						}
					},
					"boon": eval(personaname)['boon'],
					"bane": eval(personaname)['bane'],
					"team": eval(personaname)['team'],
					"level": eval(personaname)['level'],
					"xp": eval(personaname)['xp'],
					"strength": eval(personaname)['strength'],
					"magic": eval(personaname)['magic'],
					"endurance": eval(personaname)['endurance'],
					"weaponatk": eval(personaname)['weaponatk'],
					"hp": eval(personaname)['hp'],
					"currenthp": eval(personaname)['currenthp'],
					"sp": eval(personaname)['sp'],
					"currentsp": eval(personaname)['currentsp']
				}
				d = json.dumps(data)
				with open("characters/" + str(personaname) + ".json","w") as f:
					f.write(d)
					
			if int(number) == 3:
				eval(personaname)['persona']['persona3']['name'] = "n/a"
				eval(personaname)['persona']['persona3']['class'] = "n/a"
				eval(personaname)['persona']['persona3']['skill1'] = "n/a"
				eval(personaname)['persona']['persona3']['skill2'] = "n/a"
				eval(personaname)['persona']['persona3']['skill3'] = "n/a"
				eval(personaname)['persona']['persona3']['skill4'] = "n/a"
				data = {
					"firstname": eval(personaname)['firstname'],
					"lastname": eval(personaname)['lastname'],
					"class": eval(personaname)['class'],
					"persona": {
						"persona1": {
							"name": eval(personaname)['persona']['persona1']['name'],
							"class": eval(personaname)['persona']['persona1']['class'],
							"skill1": eval(personaname)['persona']['persona1']['skill1'],
							"skill2": eval(personaname)['persona']['persona1']['skill2'],
							"skill3": eval(personaname)['persona']['persona1']['skill3'],
							"skill4": eval(personaname)['persona']['persona1']['skill4']
						},
						"persona2": {
							"name": eval(personaname)['persona']['persona2']['name'],
							"class": eval(personaname)['persona']['persona2']['class'],
							"skill1": eval(personaname)['persona']['persona2']['skill1'],
							"skill2": eval(personaname)['persona']['persona2']['skill2'],
							"skill3": eval(personaname)['persona']['persona2']['skill3'],
							"skill4": eval(personaname)['persona']['persona2']['skill4']
						},
						"persona3": {
							"name": "n/a",
							"class": "n/a",
							"skill1": "n/a",
							"skill2": "n/a",
							"skill3": "n/a",
							"skill4": "n/a"
						},
						"persona4": {
							"name": eval(personaname)['persona']['persona4']['class'],
							"class": eval(personaname)['persona']['persona4']['name'],
							"skill1": eval(personaname)['persona']['persona4']['skill1'],
							"skill2": eval(personaname)['persona']['persona4']['skill2'],
							"skill3": eval(personaname)['persona']['persona4']['skill3'],
							"skill4": eval(personaname)['persona']['persona4']['skill4']
						}
					},
					"boon": eval(personaname)['boon'],
					"bane": eval(personaname)['bane'],
					"team": eval(personaname)['team'],
					"level": eval(personaname)['level'],
					"xp": eval(personaname)['xp'],
					"strength": eval(personaname)['strength'],
					"magic": eval(personaname)['magic'],
					"endurance": eval(personaname)['endurance'],
					"weaponatk": eval(personaname)['weaponatk'],
					"hp": eval(personaname)['hp'],
					"currenthp": eval(personaname)['currenthp'],
					"sp": eval(personaname)['sp'],
					"currentsp": eval(personaname)['currentsp']
				}
				d = json.dumps(data)
				with open("characters/" + str(personaname) + ".json","w") as f:
					f.write(d)
			
			if int(number) == 4:
				eval(personaname)['persona']['persona4']['name'] = "n/a"
				eval(personaname)['persona']['persona4']['class'] = "n/a"
				eval(personaname)['persona']['persona4']['skill1'] = "n/a"
				eval(personaname)['persona']['persona4']['skill2'] = "n/a"
				eval(personaname)['persona']['persona4']['skill3'] = "n/a"
				eval(personaname)['persona']['persona4']['skill4'] = "n/a"
				data = {
					"firstname": eval(personaname)['firstname'],
					"lastname": eval(personaname)['lastname'],
					"class": eval(personaname)['class'],
					"persona": {
						"persona1": {
							"name": eval(personaname)['persona']['persona1']['name'],
							"class": eval(personaname)['persona']['persona1']['class'],
							"skill1": eval(personaname)['persona']['persona1']['skill1'],
							"skill2": eval(personaname)['persona']['persona1']['skill2'],
							"skill3": eval(personaname)['persona']['persona1']['skill3'],
							"skill4": eval(personaname)['persona']['persona1']['skill4']
						},
						"persona2": {
							"name": eval(personaname)['persona']['persona2']['name'],
							"class": eval(personaname)['persona']['persona2']['class'],
							"skill1": eval(personaname)['persona']['persona2']['skill1'],
							"skill2": eval(personaname)['persona']['persona2']['skill2'],
							"skill3": eval(personaname)['persona']['persona2']['skill3'],
							"skill4": eval(personaname)['persona']['persona2']['skill4']
						},
						"persona3": {
							"name": eval(personaname)['persona']['persona3']['name'],
							"class": eval(personaname)['persona']['persona3']['class'],
							"skill1": eval(personaname)['persona']['persona3']['skill1'],
							"skill2": eval(personaname)['persona']['persona3']['skill2'],
							"skill3": eval(personaname)['persona']['persona3']['skill3'],
							"skill4": eval(personaname)['persona']['persona3']['skill4']
						},
						"persona4": {
							"name": "n/a",
							"class": "n/a",
							"skill1": "n/a",
							"skill2": "n/a",
							"skill3": "n/a",
							"skill4": "n/a"
						}
					},
					"boon": eval(personaname)['boon'],
					"bane": eval(personaname)['bane'],
					"team": eval(personaname)['team'],
					"level": eval(personaname)['level'],
					"xp": eval(personaname)['xp'],
					"strength": eval(personaname)['strength'],
					"magic": eval(personaname)['magic'],
					"endurance": eval(personaname)['endurance'],
					"weaponatk": eval(personaname)['weaponatk'],
					"hp": eval(personaname)['hp'],
					"currenthp": eval(personaname)['currenthp'],
					"sp": eval(personaname)['sp'],
					"currentsp": eval(personaname)['currentsp']
				}
				d = json.dumps(data)
				with open("characters/" + str(personaname) + ".json","w") as f:
					f.write(d)
		await bot.say("Confirmed!")

@bot.command(name="encounter")
async def _encounter(team):
	enemy = random.choice(enemylist)
	await bot.say(enemy)
	roll1 = random.randrange(1, 21)
	roll2 = random.randrange(1, 21)
	roll3 = random.randrange(1, 21)
	roll4 = random.randrange(1, 21)			
	roll5 = random.randrange(1, 21)
	roll6 = random.randrange(1, 21)
	if team.lower() == "law":
		message = "Lucas: " + str(roll1) + "\nWes: " + str(roll2) + "\nDorothy: " + str(roll3) + "\nBailey: " + str(roll4) + "\n" + enemy + ": " + str(roll5)
	if team.lower() == "chaos":
		message = "Ash: " + str(roll1) + "\nQuentin: " + str(roll2) + "\nArlo: " + str(roll3) + "\nEmily: " + str(roll4) + "\n" + enemy + ": " + str(roll5)
	await bot.say("Order:\n" + message)
	
@bot.command(name="initiative")
async def _initiative(team):
	enemy = "Enemy"
	roll1 = random.randrange(1, 21)
	roll2 = random.randrange(1, 21)
	roll3 = random.randrange(1, 21)
	roll4 = random.randrange(1, 21)			
	roll5 = random.randrange(1, 21)
	roll6 = random.randrange(1, 21)
	if team.lower() == "law":
		message = "Lucas: " + str(roll1) + "\nWes: " + str(roll2) + "\nDorothy: " + str(roll3) + "\nBailey: " + str(roll4) + "\n" + enemy + ": " + str(roll5)
	if team.lower() == "chaos":
		message = "Ash: " + str(roll1) + "\nQuentin: " + str(roll2) + "\nArlo: " + str(roll3) + "\nEmily: " + str(roll4) + "\n" + enemy + ": " + str(roll5)
	await bot.say("Order:\n" + message)
	
@bot.command(name="restore", pass_context = True)
async def _restore(ctx, team):
	if ctx.message.author.server_permissions.administrator:
		if team.lower() == "law":
			joshkinz['currenthp'] = joshkinz['hp']
			joshkinz['currentsp'] = joshkinz['sp']
			crying['currenthp'] = crying['hp']
			crying['currentsp'] = crying['sp']
			liminori['currenthp'] = liminori['hp']
			liminori['currentsp'] = liminori['sp']
			swiggle['currenthp'] = swiggle['hp']
			swiggle['currentsp'] = swiggle['sp']
		if team.lower() == "chaos":
			shadowjoe323['currenthp'] = shadowjoe323['hp']
			shadowjoe323['currentsp'] = shadowjoe323['sp']
			nintendofan['currenthp'] = nintendofan['hp']
			nintendofan['currentsp'] = nintendofan['sp']
			lord_thantus['currenthp'] = lord_thantus['hp']
			lord_thantus['currentsp'] = lord_thantus['sp']
			qlonever['currenthp'] = qlonever['hp']
			qlonever['currentsp'] = qlonever['sp']
		await bot.say("Restored!")
	
bot.run('-no lol-')
