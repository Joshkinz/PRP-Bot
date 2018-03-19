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
statusmessage = ""
partyGauge = 0

with open('skills.json') as file:
	skills = json.load(file)
with open('characters.json') as file:
	characters = json.load(file)
with open('xp.json') as file:
	xpcurve = json.load(file)

@bot.event
async def on_ready():
	print('Logged in as')
	print(bot.user.name)
	print(bot.user.id)
	print('------')

@bot.command(name="attack", pass_context = True)
async def _attack(ctx, endef, strn=1, atk=1):
	global message
	global partyGauge
	
	if strn == 1:
		strn = characters[str(ctx.message.author.name.lower())]['strength']
	if atk == 1:
		atk = characters[str(ctx.message.author.name.lower())]['weaponatk']
	
	#Set minimum and maximum values.
	if int(strn) < 1:
		strn = 1
	if int(strn) > 99:
		strn = 99
		
	if int(atk) < 1:
		atk = 1
	if int(atk) > 999:
		atk = 999
	
	if int(endef) < 1:
		endef = 1
	if int(endef) > 99:
		endef = 99
		
	#Change the variables to floats.
	strn = float(strn)
	atk = float(atk)
	endef = float(endef)
	
	#Roll for random modifiers.
	roll = random.uniform(.94, 1.06)
	critroll = random.randrange(0, 25)
	
	#Damage formula.
	damage = (5.0 * sqrt((strn * atk)) / ((sqrt(endef) / 2.0))) * roll
	
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
	partyGauge = partyGauge + (damage / 250)
	if partyGauge > 100:
		partyGauge = 100
		
	#Tell bot to post damage.
	await bot.say(message + str(int(damage)) +"\nParty gauge: " + str(int(partyGauge)) + "%!")
	message = "Total damage: "
	
	#Print a confirmation message in the console.
	print("Attack confirmed. " + str(critroll))

@bot.command(name="skill", pass_context = True)
async def _skill(ctx, name, endef, strn=1, atk=1):
	global message
	global message2
	global statusmessage
	global partyGauge
	
	if strn == 1:
		strn = characters[str(ctx.message.author.name.lower())]['strength']
	if atk == 1:
		atk = characters[str(ctx.message.author.name.lower())]['weaponatk']
		
	if skills[str(name)]['type'] == "attack":
		if int(strn) < 1:
			strn = 1
		if int(strn) > 99:
			strn = 99
			
		if int(atk) < 1:
			atk = 1
		if int(atk) > 999:
			atk = 999
		
		if int(endef) < 1:
			endef = 1
		if int(endef) > 99:
			endef = 99
			
		name = str(name)
		strn = float(strn)
		atk = float(atk)
		endef = float(endef)
	
		roll = random.uniform(.94, 1.06)
		roll = float(roll)
		roll2 = random.uniform(.94, 1.06)
		roll2 = float(roll2)
		critroll = random.randrange(0, skills[str(name)]['crit'])
		critroll2 = random.randrange(0, skills[str(name)]['crit'])
		statusroll = random.randrange(skills[str(name)]['status1'], skills[str(name)]['status2'])
		
		damage = (5.0 * sqrt((strn * atk)) / ((sqrt(endef) / 2.0))) * roll * int(skills[str(name)]['strength'])
		damage2 = (5.0 * sqrt((strn * atk)) / ((sqrt(endef) / 2.0))) * roll2 * int(skills[str(name)]['strength'])
		
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
			
		partyGauge = partyGauge + (sqrt(damage) / sqrt(endef))
		if partyGauge > 100:
			partyGauge = 100
			
		if statusroll == 1:
			statusmessage = skills[str(name)]['status']
		
		if skills[str(name)]['hits'] == 2:
			await bot.say("Hit 1: " + message + str(int(damage)) + ".\nHit 2: " + message2 + str(int(damage2)) + ".\n" + message + str(int(damage + damage2)) + ".\nDeduct " + str(skills[str(name)]['cost']) + statusmessage + "\nParty gauge: " + str(int(partyGauge)) + "%!")
		else:
			await bot.say(message + str(int(damage)) + ".\nDeduct " + str(skills[str(name)]['cost']) + ". " + statusmessage + "\nParty gauge: " + str(int(partyGauge)) + "%!")
		message = "Total damage: "
		message2 = "Total damage: "
		statusmessage = ""
			
		print(str(skills[str(name)]['name']) + " confirmed! " + str(critroll) + " " + str(statusroll))
		
	if skills[str(name)]['type'] == 'buff':
		partyGauge = int(partyGauge) + skills[str(name)]['gauge']
		await bot.say(skills[str(name)]['message'] + str(int(partyGauge)) + "%!")
		print("%s confirmed." % skills[str(name)]['name'])
		
	if skills[str(name)]['type'] == 'effect':
		statusroll = random.randrange(1, 3)
		if statusroll == 1:
			partyGauge = partyGauge + 1
			await bot.say(skills[str(name)]['message1'] + str(partyGauge) + "%!")
		else:
			await bot.say(skills[str(name)]['message2'])
		print(skills[str(name)]['name'] + " confirmed. " + str(statusroll))
		
	if skills[str(name)]['type'] == 'heal':
		if int(endef) > 999:
			endef = 999
		if int(endef) < 1:
			endef = 1
		maxhp = int(endef)
		
		bonus = (maxhp / skills[str(name)]['bonus1'])
		
		hpgiven = bonus + skills[str(name)]['bonus2']
		hpgiven = int(hpgiven)
		
		if hpgiven > maxhp:
			hpgiven = maxhp
			
		partyGauge = partyGauge + (hpgiven / 110) + 3
		if int(partyGauge) > 100:
			partyGauge = 100
		
		await bot.say("Restored " + str(hpgiven) + " HP!" +"\nDeduct 4 SP." +"\nParty gauge: " + str(int(partyGauge)) + "%!")
		
		print("%s confirmed." % skills[str(name)]['name'])
		
	if skills[str(name)]['type'] == 'revive':
		hpgiven = strn / skills[str(name)]['bonus']
		partyGauge = partyGauge + skills[str(name)]['gauge']
		await bot.say("Restored " + str(int(hpgiven)) + " HP!\nParty gauge: " + str(partyGauge) + "%!")
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
	username = ctx.message.author.name
	character = characters[str(username.lower())]
	if not name == 'a':
		character2 = characters[str(name.lower())]
		persona2 = character2['persona']
	persona = character['persona']
	if name == 'a':
		await bot.say("**STATUS**\n----------\n")
		await bot.say("Name: " + character['firstname'] + " " + character['lastname'] + "\nTeam: " + character['team'] + "\nClass: " + character['class'] + "\nHP: " + str(character['hp']) + "\nSP: " + str(character['sp']) + "\nStrength: " + str(character['strength']) + "\nMagic: " + str(character['magic']) + "\nEndurance: " + str(character['endurance']) + "\nWeapon ATK: " + str(character['weaponatk']) + "\nLevel: " + str(character['level']) + "\nXP to Next: " + str(character['xp']))
		await bot.say("**PERSONAS**\n----------")
		if not persona['persona1']['name'] == "n/a":
			await bot.say("Name 1: " + persona['persona1']['name'] + "\nClass: " + persona['persona1']['class'] + "\nSkill 1: " + persona['persona1']['skill1'] + "\nSkill 2: " + persona['persona1']['skill2'] + "\nSkill 3: " + persona['persona1']['skill3'] + "\nSkill 4: " + persona['persona1']['skill4'] + "\nLevel: " + str(persona['persona1']['level']) + "\nXP to Next: " + str(persona['persona1']['xp']))
		if not persona['persona2']['name'] == "n/a":
			await bot.say("Name 2: " + persona['persona2']['name'] + "\nClass: " + persona['persona2']['class'] + "\nSkill 1: " + persona['persona2']['skill1'] + "\nSkill 2: " + persona['persona2']['skill2'] + "\nSkill 3: " + persona['persona2']['skill3'] + "\nSkill 4: " + persona['persona2']['skill4'] + "\nLevel: " + str(persona['persona2']['level']) + "\nXP to Next: " + str(persona['persona2']['xp']))
		if not persona['persona3']['name'] == "n/a":
			await bot.say("Name 3: " + persona['persona3']['name'] + "\nClass: " + persona['persona3']['class'] + "\nSkill 1: " + persona['persona3']['skill1'] + "\nSkill 2: " + persona['persona3']['skill2'] + "\nSkill 3: " + persona['persona3']['skill3'] + "\nSkill 4: " + persona['persona3']['skill4'] + "\nLevel: " + str(persona['persona3']['level']) + "\nXP to Next: " + str(persona['persona3']['xp']))
		if not persona['persona4']['name'] == "n/a":
			await bot.say("Name 4: " + persona['persona4']['name'] + "\nClass: " + persona['persona4']['class'] + "\nSkill 1: " + persona['persona4']['skill1'] + "\nSkill 2: " + persona['persona4']['skill2'] + "\nSkill 3: " + persona['persona4']['skill3'] + "\nSkill 4: " + persona['persona4']['skill4'] + "\nLevel: " + str(persona['persona4']['level']) + "\nXP to Next: " + str(persona['persona4']['xp']))
	else:
		await bot.say("**STATUS**\n----------\n")
		await bot.say("Name: " + character2['firstname'] + " " + character2['lastname'] + "\nTeam: " + character2['team'] + "\nClass: " + character2['class'] + "\nHP: " + str(character2['hp']) + "\nSP: " + str(character2['sp']) + "\nWeapon ATK: " + str(character2['weaponatk']) + "\nLevel: " + str(character2['level']) + "\nXP to Next: " + str(character2['xp']))
		await bot.say("**PERSONAS**\n----------")
		if not persona['persona1']['name'] == "n/a":
			await bot.say("Name 1: " + persona2['persona1']['name'] + "\nClass: " + persona2['persona1']['class'] + "\nSkill 1: " + persona2['persona1']['skill1'] + "\nSkill 2: " + persona2['persona1']['skill2'] + "\nSkill 3: " + persona2['persona1']['skill3'] + "\nSkill 4: " + persona2['persona1']['skill4'] + "\nLevel: " + str(persona2['persona1']['level']) + "\nXP to Next: " + str(persona2['persona1']['xp']))
		if not persona['persona2']['name'] == "n/a":
			await bot.say("Name 2: " + persona2['persona2']['name'] + "\nClass: " + persona2['persona2']['class'] + "\nSkill 1: " + persona2['persona2']['skill1'] + "\nSkill 2: " + persona2['persona2']['skill2'] + "\nSkill 3: " + persona2['persona2']['skill3'] + "\nSkill 4: " + persona2['persona2']['skill4'] + "\nLevel: " + str(persona2['persona2']['level']) + "\nXP to Next: " + str(persona2['persona2']['xp']))
		if not persona['persona3']['name'] == "n/a":
			await bot.say("Name 3: " + persona2['persona3']['name'] + "\nClass: " + persona2['persona3']['class'] + "\nSkill 1: " + persona2['persona3']['skill1'] + "\nSkill 2: " + persona2['persona3']['skill2'] + "\nSkill 3: " + persona2['persona3']['skill3'] + "\nSkill 4: " + persona2['persona3']['skill4'] + "\nLevel: " + str(persona2['persona3']['level']) + "\nXP to Next: " + str(persona2['persona3']['xp']))
		if not persona['persona4']['name'] == "n/a":
			await bot.say("Name 4: " + persona2['persona4']['name'] + "\nClass: " + persona2['persona4']['class'] + "\nSkill 1: " + persona2['persona4']['skill1'] + "\nSkill 2: " + persona2['persona4']['skill2'] + "\nSkill 3: " + persona2['persona4']['skill3'] + "\nSkill 4: " + persona2['persona4']['skill4'] + "\nLevel: " + str(persona2['persona4']['level']) + "\nXP to Next: " + str(persona2['persona4']['xp']))

@bot.command(name="levelup", pass_context = True)
async def _levelup(ctx, name):
	if ctx.message.author.server_permissions.administrator:
		characters[str(name)]['level'] = characters[str(name)]['level'] + 1
		characters[str(name)]['xp'] = xpcurve[str(characters[str(name)]['level'])]['xp']
		if characters[str(name)]['boon'] == 'str':
			if characters[str(name)]['bane'] == 'mag':
				levelup1 = random.choice('Strength', 'Strength', 'Strength', 'Endurance', 'Endurance', 'Magic')
				levelup2 = random.choice('Strength', 'Strength', 'Strength', 'Endurance', 'Endurance', 'Magic')
			if characters[str(name)]['bane'] == 'end':
				levelup1 = random.choice('Strength', 'Strength', 'Strength', 'Endurance', 'Magic', 'Magic')
				levelup2 = random.choice('Strength', 'Strength', 'Strength', 'Endurance', 'Magic', 'Magic')
		if characters[str(name)]['boon'] == 'mag':
			if characters[str(name)]['bane'] == 'str':
				levelup1 = random.choice('Strength', 'Endurance', 'Endurance', 'Magic', 'Magic', 'Magic')
				levelup2 = random.choice('Strength', 'Endurance', 'Endurance', 'Magic', 'Magic', 'Magic')
			if characters[str(name)]['bane'] == 'end':
				levelup1 = random.choice('Strength', 'Strength', 'Endurance', 'Magic', 'Magic', 'Magic')
				levelup2 = random.choice('Strength', 'Strength', 'Endurance', 'Magic', 'Magic', 'Magic')
		if characters[str(name)]['boon'] == 'end':
			if characters[str(name)]['bane'] == 'str':
				levelup1 = random.choice('Strength', 'Endurance', 'Endurance', 'Endurance', 'Magic', 'Magic')
				levelup2 = random.choice('Strength', 'Endurance', 'Endurance', 'Endurance', 'Magic', 'Magic')
			if characters[str(name)]['bane'] == 'mag':
				levelup1 = random.choice('Strength', 'Strength', 'Endurance', 'Endurance', 'Endurance', 'Magic')
				levelup2 = random.choice('Strength', 'Strength', 'Endurance', 'Endurance', 'Endurance', 'Magic')
		await bot.say("Level up! Stats increased: " + levelup1 + "and " +levelup2)
		if levelup1 == 'Strength':
			characters[str(name)]['strength'] = characters[str(name)]['strength'] + 1
		if levelup1 == 'Magic':
			characters[str(name)]['strength'] = characters[str(name)]['magic'] + 1
		if levelup1 == 'Endurance':
			characters[str(name)]['strength'] = characters[str(name)]['endurance'] + 1
		if levelup12 == 'Strength':
			characters[str(name)]['strength'] = characters[str(name)]['strength'] + 1
		if levelup2 == 'Magic':
			characters[str(name)]['strength'] = characters[str(name)]['magic'] + 1
		if levelup2 == 'Endurance':
			characters[str(name)]['strength'] = characters[str(name)]['endurance'] + 1
	
bot.run('MzExOTY4Mzk2NjA0MzQyMjc0.DYirBA.P7vOs_Vyfhz9PRSvnQzIXS957Rk')
