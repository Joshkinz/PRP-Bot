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

@bot.event
async def on_ready():
	print('Logged in as')
	print(bot.user.name)
	print(bot.user.id)
	print('------')

@bot.command(name="attack")
async def _attack(strn, atk, endef):
	global message
	global partyGauge
	
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

@bot.command(name="skill")

#Skill List

#Lunge
#Cleave
#Giant Slice
#Megaton Raid
#God's Hand

#Double Fangs
#Myriad Slashes

#Lucky Punch
#Miracle Punch

#Agi
#Garu
#Zio
#Bufu

#Agilao
#Garula
#Zionga
#Bufula

#Agidyne
#Garudyne
#Ziodyne
#Bufudyne

#Inferno
#Panta Rhei
#Thunder Reign
#Diamond Dust

async def _skill(name, strn, atk, endef):
	global message
	global message2
	global statusmessage
	global partyGauge
		
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
	critroll = random.randrange(0, skills[str(name)]['crit'])
	critroll2 = random.randrange(0, skills[str(name)]['crit'])
	statusroll = random.randrange(skills[str(name)]['status1'], skills[str(name)]['status2'])
	
	damage = (5.0 * sqrt((strn * atk)) / ((sqrt(endef) / 2.0))) * roll * int(skills[str(name)]['strength'])
	damage2 = (5.0 * sqrt((strn * atk)) / ((sqrt(endef) / 2.0))) * roll * int(skills[str(name)]['strength'])
	
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
		await bot.say("Hit 1: " + message + str(int(damage)) + ".\nHit 2: " + message2 + str(int(damage2)) + "\n" + message + str(int(damage + damage2)) + ".\nDeduct " + str(skills[str(name)]['cost']) + " HP. " + statusmessage + "\nParty gauge: " + str(int(partyGauge)) + "%!")
	else:
		await bot.say(message + str(int(damage)) + ".\nDeduct " + str(skills[str(name)]['cost']) + " HP. " + statusmessage + "\nParty gauge: " + str(int(partyGauge)) + "%!")
	message = "Total damage: "
	message2 = "Total damage: "
	statusmessage = ""
		
	print(str(skills[str(name)]['name']) + " confirmed! " + str(critroll) + " " + str(statusroll))

@bot.command(name="buff")

#Skill List

#Tarukaja
#Rakukaja
#Heat Riser
#Tarunda
#Rakunda

#Charge
#Concentrate

#Wall
#Tetrakarn
#Makarakarn

#Amrita Drop
#Amrita Shower

async def _buff(name):
	global partyGauge
	partyGauge = int(partyGauge) + skills[str(name)]['gauge']
	await bot.say(skills[str(name)]['message'] + str(int(partyGauge)) + "%!")
	print("%s confirmed." % skills[str(name)]['name'])
	
@bot.command(name="status")

#Skill List

#Confuse
#Dormina
	
async def _status(name):
	global partyGauge
	statusroll = random.randrange(1, 3)
	if statusroll == 1:
		partyGauge = partyGauge + 1
		await bot.say(skills[str(name)]['message1'] + str(partyGauge) + "%!")
	else:
		await bot.say(skills[str(name)]['message2'])
	print(skills[str(name)]['name'] + " confirmed. " + str(statusroll))

@bot.command(name="heal")

#Skill List

#Dia
#Diarama
#Diarahan

async def _heal(name, maxhp):
	global partyGauge
	if int(maxhp) > 999:
		maxhp = 999
	if int(maxhp) < 1:
		maxhp = 1
	maxhp = int(maxhp)
	
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
	
@bot.command(name="partygauge")
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

bot.run('MzExOTY4Mzk2NjA0MzQyMjc0.DYirBA.P7vOs_Vyfhz9PRSvnQzIXS957Rk')
