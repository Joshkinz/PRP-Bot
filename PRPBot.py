import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import random
from math import sqrt

bot = Bot(command_prefix="+")
message = "Total damage: "
message2 = "Total damage: "
statusmessage = ""
partyGauge = 0

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
		
	#Change the variables to floats or strings.
	name = str(name)
	strn = float(strn)
	atk = float(atk)
	endef = float(endef)
	
	""" ------PHYSICAL ATTACKS------"""
	if name.lower() == "lunge":
		#Roll for random modifiers.
		roll = random.uniform(.94, 1.06)
		roll = float(roll)
		critroll = random.randrange(0, 25)
		
		#Damage formula.
		damage = (5.0 * sqrt((strn * atk)) / ((sqrt(endef) / 2.0))) * roll * 1.3
		
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
		partyGauge = partyGauge + (sqrt(damage) / sqrt(endef))
		if partyGauge > 100:
			partyGauge = 100
			
		#Tell bot to post damage.
		await bot.say(message + str(int(damage)) +".\nDeduct 6% HP." +"\nParty gauge: " + str(int(partyGauge)) + "%!")
		message = "Total damage: "
		
		#Print a confirmation message in the console.
		print("Lunge confirmed. " + str(critroll))
		
	if name.lower() == "cleave":
		#Roll for random modifiers.
		roll = random.uniform(.94, 1.06)
		roll = float(roll)
		critroll = random.randrange(0, 20)
		
		#Damage formula.
		damage = (5.0 * sqrt((strn * atk)) / ((sqrt(endef) / 2.0))) * roll * 1.3
		
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
		await bot.say(message + str(int(damage)) +".\nDeduct 10% HP." +"\nParty gauge: " + str(int(partyGauge)) + "%!")
		message = "Total damage: "	
			
		#Print a confirmation message in the console.
		print("Cleave confirmed. " + str(critroll))

	if name.lower() == "giantslice":
		#Roll for random modifiers.
		roll = random.uniform(.94, 1.06)
		roll = float(roll)
		critroll = random.randrange(0, 25)
		
		#Damage formula.
		damage = (5.0 * sqrt((strn * atk)) / ((sqrt(endef) / 2.0))) * roll * 2.3
		
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
		await bot.say(message + str(int(damage)) +".\nDeduct 18% HP." +"\nParty gauge: " + str(int(partyGauge)) + "%!")
		message = "Total damage: "
		
		#Print a confirmation message in the console.
		print("Giant Slice confirmed. " + str(critroll))
		
	if name.lower() == "megatonraid":
		#Roll for random modifiers.
		roll = random.uniform(.94, 1.06)
		roll = float(roll)
		critroll = random.randrange(0, 25)
		
		#Damage formula.
		damage = (5.0 * sqrt((strn * atk)) / ((sqrt(endef) / 2.0))) * roll * 2.8
		
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
		await bot.say(message + str(int(damage)) +".\nDeduct 26% HP." +"\nParty gauge: " + str(int(partyGauge)) + "%!")
		message = "Total damage: "	
			
		#Print a confirmation message in the console.
		print("Megaton Raid confirmed. " + str(critroll))
		
	if name.lower() == "godshand":
		#Roll for random modifiers.
		roll = random.uniform(.94, 1.06)
		roll = float(roll)
		critroll = random.randrange(0, 25)
		
		#Damage formula.
		damage = (5.0 * sqrt((strn * atk)) / ((sqrt(endef) / 2.0))) * roll * 4.3
		
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
		await bot.say(message + str(int(damage)) +".\nDeduct 44% HP." +"\nParty gauge: " + str(int(partyGauge)) + "%!")
		message = "Total damage: "
			
		#Print a confirmation message in the console.
		print("God's Hand confirmed. " + str(critroll))
		
	if name.lower() == "doublefangs":
		#Roll for random modifiers.
		roll1 = random.uniform(.94, 1.06)
		roll2 = random.uniform(.94, 1.06)
		roll1 = float(roll1)
		roll2 = float(roll2)
		critroll1 = random.randrange(0, 25)
		critroll2 = random.randrange(0, 25)
		
		#Damage formula.
		damage1 = (5.0 * sqrt((strn * atk)) / ((sqrt(endef) / 2.0))) * roll1 * 1.5
		damage2 = (5.0 * sqrt((strn * atk)) / ((sqrt(endef) / 2.0))) * roll2 * 1.5
		
		#Change the damage to an integer.
		damage1 = int(damage1)
		damage2 = int(damage2)
		
		#Set minimum and maximum damage.
		if damage1 < 0:
			damage1 = 0
		if damage1 > 5000:
			damage1 = 5000
		if damage2 < 0:
			damage2 = 0
		if damage2 > 5000:
			damage2 = 5000
			
		#Check for critical hit.
		if critroll1 == 1:
			#Change 'message' to reference the critical hit.
			message = "Critical hit! Total damage: "
			
			#Set critical modifier.
			damagemod1 = (sqrt(strn) / 3.5)
			
			#Set minimum and maximum critical modifier.
			if damagemod1 < 1:
				damagemod1 = 1
			if damagemod1 > 3:
				damagemod1 = 3
				
			#Apply critical modifier.
			damage1 = damage1 * damagemod1
			
		if critroll2 == 1:
			#Change 'message' to reference the critical hit.
			message = "Critical hit! Total damage: "
			
			#Set critical modifier.
			damagemod2 = (sqrt(strn) / 3.5)
			
			#Set minimum and maximum critical modifier.
			if damagemod2 < 1:
				damagemod2 = 1
			if damagemod2 > 3:
				damagemod2 = 3
				
			#Apply critical modifier.
			damage2 = damage2 * damagemod2
			
		#Set party gauge increase.
		partyGauge = partyGauge + (damage / 250)
		if partyGauge > 100:
			partyGauge = 100
			
		#Tell bot to post damage.
		await bot.say("Hit 1: " + message + str(int(damage1)) + "\nHit 2: " + message2 + str(int(damage2)) + ".\nDeduct 17% HP." +"\nParty gauge: " + str(int(partyGauge)) + "%!")
		message = "Total damage: "
		message2 = "Total damage: "
		
		#Print a confirmation message in the console.
		print("Double Fangs confirmed. " + str(critroll1) + " " + str(critroll2) +"\nParty gauge: " + str(int(partyGauge)) + "%!")
		
	if name.lower() == "myriadslashes":
		#Roll for random modifiers.
		roll1 = random.uniform(.94, 1.06)
		roll2 = random.uniform(.94, 1.06)
		roll1 = float(roll1)
		roll2 = float(roll2)
		critroll1 = random.randrange(0, 17)
		critroll2 = random.randrange(0, 17)
		
		#Damage formula.
		damage1 = (5.0 * sqrt((strn * atk)) / ((sqrt(endef) / 2.0))) * roll1 * 1.4
		damage2 = (5.0 * sqrt((strn * atk)) / ((sqrt(endef) / 2.0))) * roll2 * 1.4
		
		#Change the damage to an integer.
		damage1 = int(damage1)
		damage2 = int(damage2)
		
		#Set minimum and maximum damage.
		if damage1 < 0:
			damage1 = 0
		if damage1 > 5000:
			damage1 = 5000
		if damage2 < 0:
			damage2 = 0
		if damage2 > 5000:
			damage2 = 5000
			
		#Check for critical hit.
		if critroll1 == 1:
			#Change 'message' to reference the critical hit.
			message = "Critical hit! Total damage: "
			
			#Set critical modifier.
			damagemod1 = (sqrt(strn) / 3.5)
			
			#Set minimum and maximum critical modifier.
			if damagemod1 < 1:
				damagemod1 = 1
			if damagemod1 > 3:
				damagemod1 = 3
				
			#Apply critical modifier.
			damage1 = damage1 * damagemod1
			
		if critroll2 == 1:
			#Change 'message' to reference the critical hit.
			message2 = "Critical hit! Total damage: "
			
			#Set critical modifier.
			damagemod2 = (sqrt(strn) / 3.5)
			
			#Set minimum and maximum critical modifier.
			if damagemod2 < 1:
				damagemod2 = 1
			if damagemod2 > 3:
				damagemod2 = 3
				
			#Apply critical modifier.
			damage2 = damage2 * damagemod2
			
		#Set party gauge increase.
		partyGauge = partyGauge + (damage / 250)
		if partyGauge > 100:
			partyGauge = 100
			
		#Tell bot to post damage.
		await bot.say("Hit 1: " + message + str(int(damage1)) + "\nHit 2: " + message2 + str(int(damage2)) + ".\nDeduct 22% HP." +"\nParty gauge: " + str(int(partyGauge)) + "%!")
		message = "Total damage: "
		message2 = "Total damage: "
			
		#Print a confirmation message in the console.
		print("Myriad Slashes confirmed. " + str(critroll1) + " " + str(critroll2))
		
	if name.lower() == "luckypunch":
		#Roll for random modifiers.
		roll = random.uniform(.94, 1.06)
		roll = float(roll)
		critroll = random.randrange(1, 5)
		
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
		await bot.say(message + str(int(damage)) +".\nDeduct 20% HP." +"\nParty gauge: " + str(int(partyGauge)) + "%!")
		message = "Total damage: "

		#Print a confirmation message in the console.
		print("Lucky Punch confirmed. " + str(critroll))
		
	if name.lower() == "miraclepunch":
		#Roll for random modifiers.
		roll = random.uniform(.94, 1.06)
		roll = float(roll)
		critroll = random.randrange(1, 3)
		
		#Damage formula.
		damage = (5.0 * sqrt((strn * atk)) / ((sqrt(endef) / 2.0))) * roll * 1.4
		
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
		await bot.say(message + str(int(damage)) +".\nDeduct 35% HP." +"\nParty gauge: " + str(int(partyGauge)) + "%!")
		message = "Total damage: "

		#Print a confirmation message in the console.
		print("Miracle Punch confirmed. " + str(critroll))
		
	"""------MAGIC ATTACKS------"""
	if name.lower() == "agi":
		#Roll for random modifiers.
		roll = random.uniform(.94, 1.06)
		roll = float(roll)
		critroll = random.randrange(1, 30)
		statusroll = random.randrange(1, 11)
		
		#Damage formula.
		damage = (5.0 * sqrt((strn * atk)) / ((sqrt(endef) / 2.0))) * roll * 1.4
		
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
		
		#Check for status effect.
		if statusroll == 1:
			#Change 'message2' to reference the effect.
			statusmessage = "Burn applied! Target takes 2% HP damage per turn for 4 turns."
			
		#Set party gauge increase.
		partyGauge = partyGauge + (damage / 250)
		if partyGauge > 100:
			partyGauge = 100
			
		#Tell bot to post damage.
		await bot.say(message + str(int(damage)) +".\nDeduct 4 SP." +" " + statusmessage +"\nParty gauge: " + str(int(partyGauge)) + "%!")
		message = "Total damage: "
		statusmessage = ""
		
		#Print a confirmation message in the console.
		print("Agi confirmed. " + str(critroll) + " " + str(statusroll))
		
	if name.lower() == "agilao":
		#Roll for random modifiers.
		roll = random.uniform(.94, 1.06)
		roll = float(roll)
		critroll = random.randrange(1, 30)
		statusroll = random.randrange(1, 11)
		
		#Damage formula.
		damage = (5.0 * sqrt((strn * atk)) / ((sqrt(endef) / 2.0))) * roll * 1.9
		
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
		
		#Check for status effect.
		if statusroll == 1:
			#Change 'message2' to reference the effect.
			statusmessage = "Burn applied! Target takes 2% HP damage per turn for 4 turns."
			
		#Set party gauge increase.
		partyGauge = partyGauge + (damage / 250)
		if partyGauge > 100:
			partyGauge = 100
			
		#Tell bot to post damage.
		await bot.say(message + str(int(damage)) +".\nDeduct 8 SP." +" " + statusmessage +"\nParty gauge: " + str(int(partyGauge)) + "%!")
		message = "Total damage: "
		statusmessage = ""
		
		#Print a confirmation message in the console.
		print("Agilao confirmed. " + str(critroll) + " " + str(statusroll))
		
	if name.lower() == "agidyne":
		#Roll for random modifiers.
		roll = random.uniform(.94, 1.06)
		roll = float(roll)
		critroll = random.randrange(1, 30)
		statusroll = random.randrange(1, 11)
		
		#Damage formula.
		damage = (5.0 * sqrt((strn * atk)) / ((sqrt(endef) / 2.0))) * roll * 2.6
		
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
		
		#Check for status effect.
		if statusroll == 1:
			#Change 'message2' to reference the effect.
			statusmessage = "Burn applied! Target takes 2% HP damage per turn for 4 turns."
			
		#Set party gauge increase.
		partyGauge = partyGauge + (damage / 250)
		if partyGauge > 100:
			partyGauge = 100
			
		#Tell bot to post damage.
		await bot.say(message + str(int(damage)) +".\nDeduct 12 SP." +" " + statusmessage +"\nParty gauge: " + str(int(partyGauge)) + "%!")
		message = "Total damage: "
		statusmessage = ""
		
		#Print a confirmation message in the console.
		print("Agidyne confirmed. " + str(critroll) + " " + str(statusroll))
		
	if name.lower() == "inferno":
		#Roll for random modifiers.
		roll = random.uniform(.94, 1.06)
		roll = float(roll)
		critroll = random.randrange(1, 30)
		statusroll = random.randrange(1, 7)
		
		#Damage formula.
		damage = (5.0 * sqrt((strn * atk)) / ((sqrt(endef) / 2.0))) * roll * 4.0
		
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
		
		#Check for status effect.
		if statusroll == 1:
			#Change 'message2' to reference the effect.
			statusmessage = "Burn applied! Target takes 2% HP damage per turn for 4 turns."
			
		#Set party gauge increase.
		partyGauge = partyGauge + (damage / 250)
		if partyGauge > 100:
			partyGauge = 100
			
		#Tell bot to post damage.
		await bot.say(message + str(int(damage)) +".\nDeduct 40 SP." +" " + statusmessage +"\nParty gauge: " + str(int(partyGauge)) + "%!")
		message = "Total damage: "
		statusmessage = ""
		
		#Print a confirmation message in the console.
		print("Inferno confirmed. " + str(critroll) + " " + str(statusroll))
		
	if name.lower() == "garu":
		#Roll for random modifiers.
		roll = random.uniform(.94, 1.06)
		roll = float(roll)
		critroll = random.randrange(1, 30)
		statusroll = random.randrange(1, 11)
		
		#Damage formula.
		damage = (5.0 * sqrt((strn * atk)) / ((sqrt(endef) / 2.0))) * roll * 1.4
		
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
		
		#Check for status effect.
		if statusroll == 1:
			#Change 'message2' to reference the effect.
			statusmessage = "Dizzy applied! Target deals only 60% damage per turn for 2 turns."
			
		#Set party gauge increase.
		partyGauge = partyGauge + (damage / 250)
		if partyGauge > 100:
			partyGauge = 100
			
		#Tell bot to post damage.
		await bot.say(message + str(int(damage)) +".\nDeduct 4 SP." +" " + statusmessage +"\nParty gauge: " + str(int(partyGauge)) + "%!")
		message = "Total damage: "
		statusmessage = ""
		
		#Print a confirmation message in the console.
		print("Garu confirmed. " + str(critroll) + " " + str(statusroll))
		
	if name.lower() == "garula":
		#Roll for random modifiers.
		roll = random.uniform(.94, 1.06)
		roll = float(roll)
		critroll = random.randrange(1, 30)
		statusroll = random.randrange(1, 11)
		
		#Damage formula.
		damage = (5.0 * sqrt((strn * atk)) / ((sqrt(endef) / 2.0))) * roll * 1.9
		
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
		
		#Check for status effect.
		if statusroll == 1:
			#Change 'message2' to reference the effect.
			statusmessage = "Dizzy applied! Target deals only 60% damage per turn for 2 turns."
			
		#Set party gauge increase.
		partyGauge = partyGauge + (damage / 250)
		if partyGauge > 100:
			partyGauge = 100
			
		#Tell bot to post damage.
		await bot.say(message + str(int(damage)) +".\nDeduct 8 SP." +" " + statusmessage +"\nParty gauge: " + str(int(partyGauge)) + "%!")
		message = "Total damage: "
		statusmessage = ""
		
		#Print a confirmation message in the console.
		print("Garula confirmed. " + str(critroll) + " " + str(statusroll))
		
	if name.lower() == "garudyne":
		#Roll for random modifiers.
		roll = random.uniform(.94, 1.06)
		roll = float(roll)
		critroll = random.randrange(1, 30)
		statusroll = random.randrange(1, 11)
		
		#Damage formula.
		damage = (5.0 * sqrt((strn * atk)) / ((sqrt(endef) / 2.0))) * roll * 2.6
		
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
		
		#Check for status effect.
		if statusroll == 1:
			#Change 'message2' to reference the effect.
			statusmessage = "Dizzy applied! Target deals only 60% damage per turn for 2 turns."
			
		#Set party gauge increase.
		partyGauge = partyGauge + (damage / 250)
		if partyGauge > 100:
			partyGauge = 100
			
		#Tell bot to post damage.
		await bot.say(message + str(int(damage)) +".\nDeduct 12 SP." +" " + statusmessage +"\nParty gauge: " + str(int(partyGauge)) + "%!")
		message = "Total damage: "
		statusmessage = ""
		
		#Print a confirmation message in the console.
		print("Garudyne confirmed. " + str(critroll) + " " + str(statusroll))
		
	if name.lower() == "pantarhei":
		#Roll for random modifiers.
		roll = random.uniform(.94, 1.06)
		roll = float(roll)
		critroll = random.randrange(1, 30)
		statusroll = random.randrange(1, 7)
		
		#Damage formula.
		damage = (5.0 * sqrt((strn * atk)) / ((sqrt(endef) / 2.0))) * roll * 4.0
		
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
		
		#Check for status effect.
		if statusroll == 1:
			#Change 'message2' to reference the effect.
			statusmessage = "Dizzy applied! Target deals only 60% damage per turn for 2 turns."
			
		#Set party gauge increase.
		partyGauge = partyGauge + (damage / 250)
		if partyGauge > 100:
			partyGauge = 100
			
		#Tell bot to post damage.
		await bot.say(message + str(int(damage)) +".\nDeduct 40 SP." +" " + statusmessage +"\nParty gauge: " + str(int(partyGauge)) + "%!")
		message = "Total damage: "
		statusmessage = ""
		
		#Print a confirmation message in the console.
		print("Panta Rhei confirmed. " + str(critroll) + " " + str(statusroll))
		
	if name.lower() == "zio":
		#Roll for random modifiers.
		roll = random.uniform(.94, 1.06)
		roll = float(roll)
		critroll = random.randrange(1, 30)
		statusroll = random.randrange(1, 11)
		
		#Damage formula.
		damage = (5.0 * sqrt((strn * atk)) / ((sqrt(endef) / 2.0))) * roll * 1.4
		
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
		
		#Check for status effect.
		if statusroll == 1:
			#Change 'message2' to reference the effect.
			statusmessage = "Shock applied! Target can not move for 3 turns, but all who touch the target while it is Shocked suffer 100 HP damage."
			
		#Set party gauge increase.
		partyGauge = partyGauge + (damage / 250)
		if partyGauge > 100:
			partyGauge = 100
			
		#Tell bot to post damage.
		await bot.say(message + str(int(damage)) +".\nDeduct 4 SP." +" " + statusmessage +"\nParty gauge: " + str(int(partyGauge)) + "%!")
		message = "Total damage: "
		statusmessage = ""
		
		#Print a confirmation message in the console.
		print("Zio confirmed. " + str(critroll) + " " + str(statusroll))
		
	if name.lower() == "zionga":
		#Roll for random modifiers.
		roll = random.uniform(.94, 1.06)
		roll = float(roll)
		critroll = random.randrange(1, 30)
		statusroll = random.randrange(1, 11)
		
		#Damage formula.
		damage = (5.0 * sqrt((strn * atk)) / ((sqrt(endef) / 2.0))) * roll * 1.9
		
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
		
		#Check for status effect.
		if statusroll == 1:
			#Change 'message2' to reference the effect.
			statusmessage = "Shock applied! Target can not move for 3 turns, but all who touch the target while it is Shocked suffer 100 HP damage."
			
		#Set party gauge increase.
		partyGauge = partyGauge + (damage / 250)
		if partyGauge > 100:
			partyGauge = 100
			
		#Tell bot to post damage.
		await bot.say(message + str(int(damage)) +".\nDeduct 8 SP." +" " + statusmessage +"\nParty gauge: " + str(int(partyGauge)) + "%!")
		message = "Total damage: "
		statusmessage = ""
		
		#Print a confirmation message in the console.
		print("Zionga confirmed. " + str(critroll) + " " + str(statusroll))
		
	if name.lower() == "ziodyne":
		#Roll for random modifiers.
		roll = random.uniform(.94, 1.06)
		roll = float(roll)
		critroll = random.randrange(1, 30)
		statusroll = random.randrange(1, 11)
		
		#Damage formula.
		damage = (5.0 * sqrt((strn * atk)) / ((sqrt(endef) / 2.0))) * roll * 2.6
		
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
		
		#Check for status effect.
		if statusroll == 1:
			#Change 'message2' to reference the effect.
			statusmessage = "Shock applied! Target can not move for 3 turns, but all who touch the target while it is Shocked suffer 100 HP damage."
			
		#Set party gauge increase.
		partyGauge = partyGauge + (damage / 250)
		if partyGauge > 100:
			partyGauge = 100
			
		#Tell bot to post damage.
		await bot.say(message + str(int(damage)) +".\nDeduct 12 SP." +" " + statusmessage +"\nParty gauge: " + str(int(partyGauge)) + "%!")
		message = "Total damage: "
		statusmessage = ""
		
		#Print a confirmation message in the console.
		print("Ziodyne confirmed. " + str(critroll) + " " + str(statusroll))
		
	if name.lower() == "thunderreign":
		#Roll for random modifiers.
		roll = random.uniform(.94, 1.06)
		roll = float(roll)
		critroll = random.randrange(1, 30)
		statusroll = random.randrange(1, 7)
		
		#Damage formula.
		damage = (5.0 * sqrt((strn * atk)) / ((sqrt(endef) / 2.0))) * roll * 4.0
		
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
		
		#Check for status effect.
		if statusroll == 1:
			#Change 'message2' to reference the effect.
			statusmessage = "Shock applied! Target can not move for 3 turns, but all who touch the target while it is shocked suffer 100 HP damage."
			
		#Set party gauge increase.
		partyGauge = partyGauge + (damage / 250)
		if partyGauge > 100:
			partyGauge = 100
			
		#Tell bot to post damage.
		await bot.say(message + str(int(damage)) +".\nDeduct 40 SP." +" " + statusmessage +"\nParty gauge: " + str(int(partyGauge)) + "%!")
		message = "Total damage: "
		statusmessage = ""
		
		#Print a confirmation message in the console.
		print("Thunder Reign confirmed. " + str(critroll) + " " + str(statusroll))
		
	if name.lower() == "bufu":
		#Roll for random modifiers.
		roll = random.uniform(.94, 1.06)
		roll = float(roll)
		critroll = random.randrange(1, 30)
		statusroll = random.randrange(1, 11)
		
		#Damage formula.
		damage = (5.0 * sqrt((strn * atk)) / ((sqrt(endef) / 2.0))) * roll * 1.4
		
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
		
		#Check for status effect.
		if statusroll == 1:
			#Change 'message2' to reference the effect.
			statusmessage = "Freeze applied! Target can not move during its next turn."
			
		#Set party gauge increase.
		partyGauge = partyGauge + (damage / 250)
		if partyGauge > 100:
			partyGauge = 100
			
		#Tell bot to post damage.
		await bot.say(message + str(int(damage)) +".\nDeduct 4 SP." +" " + statusmessage +"\nParty gauge: " + str(int(partyGauge)) + "%!")
		message = "Total damage: "
		statusmessage = ""
		
		#Print a confirmation message in the console.
		print("Bufu confirmed. " + str(critroll) + " " + str(statusroll))
		
	if name.lower() == "bufula":
		#Roll for random modifiers.
		roll = random.uniform(.94, 1.06)
		roll = float(roll)
		critroll = random.randrange(1, 30)
		statusroll = random.randrange(1, 11)
		
		#Damage formula.
		damage = (5.0 * sqrt((strn * atk)) / ((sqrt(endef) / 2.0))) * roll * 1.9
		
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
		
		#Check for status effect.
		if statusroll == 1:
			#Change 'message2' to reference the effect.
			statusmessage = "Freeze applied! Target can not move during its next turn."
			
		#Set party gauge increase.
		partyGauge = partyGauge + (damage / 250)
		if partyGauge > 100:
			partyGauge = 100
			
		#Tell bot to post damage.
		await bot.say(message + str(int(damage)) +".\nDeduct 8 SP." +" " + statusmessage +"\nParty gauge: " + str(int(partyGauge)) + "%!")
		message = "Total damage: "
		statusmessage = ""
		
		#Print a confirmation message in the console.
		print("Bufula confirmed. " + str(critroll) + " " + str(statusroll))
		
	if name.lower() == "bufudyne":
		#Roll for random modifiers.
		roll = random.uniform(.94, 1.06)
		roll = float(roll)
		critroll = random.randrange(1, 30)
		statusroll = random.randrange(1, 11)
		
		#Damage formula.
		damage = (5.0 * sqrt((strn * atk)) / ((sqrt(endef) / 2.0))) * roll * 2.6
		
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
		
		#Check for status effect.
		if statusroll == 1:
			#Change 'message2' to reference the effect.
			statusmessage = "Freeze applied! Target can not move during its next turn."
			
		#Set party gauge increase.
		partyGauge = partyGauge + (damage / 250)
		if partyGauge > 100:
			partyGauge = 100
			
		#Tell bot to post damage.
		await bot.say(message + str(int(damage)) +".\nDeduct 12 SP." +" " + statusmessage +"\nParty gauge: " + str(int(partyGauge)) + "%!")
		message = "Total damage: "
		statusmessage = ""
		
		#Print a confirmation message in the console.
		print("Bufudyne confirmed. " + str(critroll) + " " + str(statusroll))
		
	if name.lower() == "diamonddust":
		#Roll for random modifiers.
		roll = random.uniform(.94, 1.06)
		roll = float(roll)
		critroll = random.randrange(1, 30)
		statusroll = random.randrange(1, 7)
		
		#Damage formula.
		damage = (5.0 * sqrt((strn * atk)) / ((sqrt(endef) / 2.0))) * roll * 4.0
		
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
		
		#Check for status effect.
		if statusroll == 1:
			#Change 'message2' to reference the effect.
			statusmessage = "Freeze applied! Target can not move during its next turn."
			
		#Set party gauge increase.
		partyGauge = partyGauge + (damage / 250)
		if partyGauge > 100:
			partyGauge = 100
			
		#Tell bot to post damage.
		await bot.say(message + str(int(damage)) +".\nDeduct 40 SP." +" " + statusmessage +"\nParty gauge: " + str(int(partyGauge)) + "%!")
		message = "Total damage: "
		statusmessage = ""
		
		#Print a confirmation message in the console.
		print("Diamond Dust confirmed. " + str(critroll) + " " + str(statusroll))
		
@bot.command(name="buff")

#Skill List

#Tarukaja
#Rakukaja
#Heat Riser
#Tarunda
#Rakunda

#Charge
#Concentrate

#Wall------For bot purposes only. Actual skills are Fire Wall, Ice Wall, Elec Wall, and Wind Wall.
#Tetrakarn
#Makarakarn

async def _buff(name):
	global partyGauge
	if name.lower() == "tarukaja":
		partyGauge = int(partyGauge) + 4
		await bot.say("Target's Strength x1.5 for 3 turns.\nDeduct 8 SP.\nParty gauge: " + str(int(partyGauge)) + "%!")
		print("Tarukaja confirmed.")
		
	if name.lower() == "rakukaja":
		partyGauge = int(partyGauge) + 4
		await bot.say("Target's Defense x1.5 for 3 turns.\nDeduct 8 SP.\nParty gauge: " + str(int(partyGauge)) + "%!")
		print("Rakukaja confirmed.")
		
	if name.lower() == "heatriser":
		partyGauge = int(partyGauge) + 8
		await bot.say("Target's Strength and Defense x1.5 for 2 turns.\nDeduct 30 SP.\nParty gauge: " + str(int(partyGauge)) + "%!")
		print("Heat Riser confirmed.")
		
	if name.lower() == "tarunda":
		partyGauge = int(partyGauge) + 2
		await bot.say("Target's Strength x0.5 for 3 turns.\nDeduct 8 SP.\nParty gauge: " + str(int(partyGauge)) + "%!")
		print("Rakukaja confirmed.")
		
	if name.lower() == "rakunda":
		partyGauge = int(partyGauge) + 2
		await bot.say("Target's Defense x0.5 for 3 turns.\nDeduct 8 SP.\nParty gauge: " + str(int(partyGauge)) + "%!")
		print("Rakukaja confirmed.")
		
	if name.lower() == "charge":
		partyGauge = int(partyGauge) + 5
		await bot.say("Target's next **physical** attack x2.5.\nDeduct 15 SP.\nParty gauge: " + str(int(partyGauge)) + "%!")
		print("Charge confirmed.")
		
	if name.lower() == "concentrate":
		partyGauge = int(partyGauge) + 5
		await bot.say("Target's next **magic** attack x2.5.\nDeduct 15 SP.\nParty gauge: " + str(int(partyGauge)) + "%!")
		print("Concentrate confirmed.")
		
	if name.lower() == "wall":
		partyGauge = int(partyGauge) + 4
		await bot.say("Target's innate elemental weaknesses are negated for 3 turns.\nDeduct 18 SP.\nParty gauge: " + str(int(partyGauge)) + "%!")
		print("Wall confirmed.")
		
	if name.lower() == "tetrakarn":
		partyGauge = int(partyGauge) + 6
		await bot.say("Target repels next **physical** attack.\nDeduct 36 SP.\nParty gauge: " + str(int(partyGauge)) + "%!")
		print("Tetrakarn confirmed.")
		
	if name.lower() == "makarakarn":
		partyGauge = int(partyGauge) + 6
		await bot.say("Target repels next **magic** attack.\nDeduct 36 SP.\nParty gauge: " + str(int(partyGauge)) + "%!")
		print("Charge confirmed.")
		
@bot.command(name="heal")

#Skill List

#Dia
#Diarama
#Diarahan

#Recarm
#Samarecarm

#Amrita Drop
#Amrita Shower

async def _heal(name, maxhp):
	global partyGauge
	if int(maxhp) > 999:
		maxhp = 999
	if int(maxhp) < 1:
		maxhp = 1
	name = str(name)
	maxhp = int(maxhp)
	if name.lower() == "dia":
		#Set the bonus HP given.
		bonus = (maxhp / 4)
		
		#Add bonus HP to the base value.
		hpgiven = bonus + 30
		hpgiven = int(hpgiven)
		
		#Set a cap on the HP restored.
		if hpgiven > maxhp:
			hpgiven = maxhp
			
		#Set party gauge increase.
		partyGauge = partyGauge + (hpgiven / 110) + 3
		if int(partyGauge) > 100:
			partyGauge = 100
		
		#Tell bot to post HP restored.
		await bot.say("Restored " + str(hpgiven) + " HP!" +"\nDeduct 4 SP." +"\nParty gauge: " + str(int(partyGauge)) + "%!")
		
		#Print a confirmation message in the console.
		print("Dia confirmed.")
		
	if name.lower() == "diarama":
		#Set the bonus HP given.
		bonus = (maxhp / 2)
		
		#Add bonus HP to the base value.
		hpgiven = bonus + 75
		hpgiven = int(hpgiven)
		
		#Set a cap on the HP restored.
		if hpgiven > maxhp:
			hpgiven = maxhp
			
		#Set party gauge increase.
		partyGauge = partyGauge + (hpgiven / 100) + 4
		if int(partyGauge) > 100:
			partyGauge = 100
			
		#Tell bot to post HP restored.
		await bot.say("Restored " + str(hpgiven) + " HP!" +"\nDeduct 8 SP." +"\nParty gauge: " + str(int(partyGauge)) + "%!")
		
		#Print a confirmation message in the console.
		print("Diarama confirmed.")
		
	if name.lower() == "diarahan":
		#Diarahan just restores maximum HP.
		
		#Set party gauge increase.
		partyGauge = partyGauge + (maxhp / 90) + 5
		if int(partyGauge) > 100:
			partyGauge = 100
		
		#Tell the bot to post HP restored.
		await bot.say("Restored " + str(maxhp) + " HP!" +"\nDeduct 12 SP." +"\nParty gauge: " + str(int(partyGauge)) + "%!")
		
		#Print a confirmation message in the console.
		print("Diarahan confirmed.")
		
	if name.lower() == "recarm":
		#Revives with 50% HP
		
		#Set party gauge increase.
		partyGauge = partyGauge + 6
		if int(partyGauge) > 100:
			partyGauge = 100
			
		hpgiven = (maxhp / 2)
		hpgiven = int(hpgiven)
		
		#Tell the bot to post HP restored.
		await bot.say("Revived with " + str(hpgiven) + " HP!" +"\nDeduct 8 SP." +"\nParty gauge: " + str(int(partyGauge)) + "%!")
		
		#Print a confirmation message in the console.
		print("Recarm confirmed.")
		
	if name.lower() == "samarecarm":
		#Revives with full HP.
		
		#Set party gauge increase.
		partyGauge = partyGauge + 12
		if int(partyGauge) > 100:
			partyGauge = 100
		
		#Tell the bot to post HP restored.
		await bot.say("Revived with " + str(maxhp) + " HP!" +"\nDeduct 16 SP." +"\nParty gauge: " + str(int(partyGauge)) + "%!")
		
		#Print a confirmation message in the console.
		print("Samarecarm confirmed.")
		
@bot.command(name="status")

#Skill List

#Confuse
#Dormina

async def _status(name):
	global partyGauge
	if name.lower() == "confuse":
		roll = random.randrange(1, 3)
		if roll == 1:
			partyGauge = int(partyGauge) + 1
			await bot.say("Target successfully confused! It is unable to choose a target for 3 turns.\nDeduct 5 SP.\nParty gauge: " + str(int(partyGauge)) + "%!")
		else:
			await bot.say("Confuse missed!")
		print("Confuse confirmed. " + str(int(roll)))
			
	if name.lower() == "dormina":
		roll = random.randrange(1, 3)
		if roll == 1:
			partyGauge = int(partyGauge) + 1
			await bot.say("Target is asleep! It is unable to act for 2 turns.\nDeduct 5 SP.\nParty gauge: " + str(int(partyGauge)) + "%!")
		else:
			await bot.say("Dormina missed!")
		print("Dormina confirmed. " + str(int(roll)))
		
	if name.lower() == "amritadrop":
		#Cures all ailments of 1 target.
		
		partyGauge = partyGauge + 4
		if int(partyGauge) < 1:
			partyGauge = 1
		if int(partyGauge) > 100:
			partyGauge = 100
		await bot.say("Target cured of all ailments!\nDeduct 6SP.\nParty gauge: " + str(int(partyGauge)) + "%!")
		print("Amrita Drop confirmed.")
		
	if name.lower() == "amritashower":
		#Cures all ailments of party.
		
		partyGauge = partyGauge + 10
		if int(partyGauge) < 1:
			partyGauge = 1
		if int(partyGauge) > 100:
			partyGauge = 100
		await bot.say("Party cured of all ailments!\nDeduct 15SP.\nParty gauge: " + str(int(partyGauge)) + "%!")
		print("Amrita Shower confirmed.")
		
@bot.command(name="partygauge")
async def _partygauge(name):
	global partyGauge
	if name.lower() == "check":
		#Tell the bot to post the Party Gauge status.
		await bot.say("Party gauge: " + str(int(partyGauge)) + "%!")
		
		#Print a confirmation message in the console.
		print("PG Check confirmed.")
	
	if name.lower() == "teamwork":
		#Check if there is enough gauge.
		
		#If there is not enough gauge, it fails.	
		if int(partyGauge) < 33:
			#Tell the bot to post the failure message.
			await bot.say("Not enough charge!\nParty gauge: " + str(int(partyGauge)) + "%!")
			
			#Print a failure message in the console.
			print("Teamwork attack failed.")
		
		if int(partyGauge) > 32:
			#Subtract the now-used gauge.
			partyGauge = int(partyGauge - 33)
			if int(partyGauge) < 0:
				partyGauge = 1
				
			#Tell the bot to post a confirmation.
			await bot.say("Teamwork attack initiated!\nParty gauge: " + str(int(partyGauge)) + "%!")
			
			#Print a confirmation message in the console.
			print("Teamwork Attack confirmed.")
			
	if name.lower() == "chain":
		if int(partyGauge) > 99:
			partyGauge = int(partyGauge - 100)
			if int(partyGauge) < 0:
				partyGauge = 1
			await bot.say("Chain attack initiated!\nParty gauge: " + str(int(partyGauge)) + "%!")
			print("Chain Attack confirmed.")
			
		if int(partyGauge) < 100:
			await bot.say("Not enough charge!\nParty gauge: " + str(int(partyGauge)) + "%!")
			print("Chain attack failed.")
					
@bot.command(name="gauge")
async def _gauge(name, number):
	global partyGauge
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

bot.run('-snip-')
