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
		if damagemod < 1:
			damagemod = 1
		if damagemod > 3:
			damagemod = 3
		
		#Apply critical modifier.
		damage = damage * damagemod
		
	#Tell bot to post damage.
	await bot.say(message + str(int(damage)))
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

#Dia
#Diarama
#Diarahan

async def _skill(name, strn, atk, endef):
	global message
	global message2
	global statusmessage
	#Change the variables to floats or strings.
	name = str(name)
	strn = float(strn)
	atk = float(atk)
	endef = float(endef)
	
	""" ------PHYSICAL ATTACKS------"""
	if name == "lunge":
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
			if damagemod < 1:
				damagemod = 1
			if damagemod > 3:
				damagemod = 3
				
			#Apply critical modifier.
			damage = damage * damagemod
			
		#Tell bot to post damage.
		await bot.say(message + str(int(damage)) +".\nDeduct 6% HP.")
		message = "Total damage: "
		
		#Print a confirmation message in the console.
		print("Lunge confirmed. " + str(critroll))
		
	if name == "cleave":
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
			if damagemod < 1:
				damagemod = 1
			if damagemod > 3:
				damagemod = 3
				
			#Apply critical modifier.
			damage = damage * damagemod
			
		#Tell bot to post damage.
		await bot.say(message + str(int(damage)) +".\nDeduct 10% HP.")
		message = "Total damage: "	
			
		#Print a confirmation message in the console.
		print("Cleave confirmed. " + str(critroll))

	if name == "giantslice":
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
			if damagemod < 1:
				damagemod = 1
			if damagemod > 3:
				damagemod = 3
				
			#Apply critical modifier.
			damage = damage * damagemod
			
		#Tell bot to post damage.
		await bot.say(message + str(int(damage)) +".\nDeduct 18% HP.")
		message = "Total damage: "
		
		#Print a confirmation message in the console.
		print("Giant Slice confirmed. " + str(critroll))
		
	if name == "megatonraid":
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
			if damagemod < 1:
				damagemod = 1
			if damagemod > 3:
				damagemod = 3
				
			#Apply critical modifier.
			damage = damage * damagemod
			
		#Tell bot to post damage.
		await bot.say(message + str(int(damage)) +".\nDeduct 26% HP.")
		message = "Total damage: "	
			
		#Print a confirmation message in the console.
		print("Megaton Raid confirmed. " + str(critroll))
		
	if name == "godshand":
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
			if damagemod < 1:
				damagemod = 1
			if damagemod > 3:
				damagemod = 3
				
			#Apply critical modifier.
			damage = damage * damagemod
			
		#Tell bot to post damage.
		await bot.say(message + str(int(damage)) +".\nDeduct 44% HP.")
		message = "Total damage: "
			
		#Print a confirmation message in the console.
		print("God's Hand confirmed. " + str(critroll))
		
	if name == "doublefangs":
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
			
		#Tell bot to post damage.
		await bot.say("Hit 1: " + message + str(int(damage1)) + "\nHit 2: " + message2 + str(int(damage2)) + ".\nDeduct 17% HP.")
		message = "Total damage: "
		message2 = "Total damage: "
		
		#Print a confirmation message in the console.
		print("Double Fangs confirmed. " + str(critroll1) + " " + str(critroll2))
		
	if name == "myriadslashes":
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
			
		#Tell bot to post damage.
		await bot.say("Hit 1: " + message + str(int(damage1)) + "\nHit 2: " + message2 + str(int(damage2)) + ".\nDeduct 22% HP.")
		message = "Total damage: "
		message2 = "Total damage: "
			
		#Print a confirmation message in the console.
		print("Myriad Slashes confirmed. " + str(critroll1) + " " + str(critroll2))
		
	if name == "luckypunch":
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
			if damagemod < 1:
				damagemod = 1
			if damagemod > 3:
				damagemod = 3
				
			#Apply critical modifier.
			damage = damage * damagemod
			
		#Tell bot to post damage.
		await bot.say(message + str(int(damage)) +".\nDeduct 20% HP.")
		message = "Total damage: "

		#Print a confirmation message in the console.
		print("Lucky Punch confirmed. " + str(critroll))
		
	if name == "miraclepunch":
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
			if damagemod < 1:
				damagemod = 1
			if damagemod > 3:
				damagemod = 3
				
			#Apply critical modifier.
			damage = damage * damagemod
			
		#Tell bot to post damage.
		await bot.say(message + str(int(damage)) +".\nDeduct 35% HP.")
		message = "Total damage: "

		#Print a confirmation message in the console.
		print("Miracle Punch confirmed. " + str(critroll))
		
	"""------MAGIC ATTACKS------"""
	if name == "agi":
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
			if damagemod < 1:
				damagemod = 1
			if damagemod > 3:
				damagemod = 3
				
			#Apply critical modifier.
			damage = damage * damagemod
		
		#Check for status effect.
		if statusroll == 1:
			#Change 'message2' to reference the effect.
			statusmessage = "Burn applied! Target takes 2% HP damage per turn for 4 turns."
			
		#Tell bot to post damage.
		await bot.say(message + str(int(damage)) +".\nDeduct 4 SP." +" " + statusmessage)
		message = "Total damage: "
		statusmessage = ""
		
		#Print a confirmation message in the console.
		print("Agi confirmed. " + str(critroll) + " " + str(statusroll))
		
	if name == "agilao":
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
			if damagemod < 1:
				damagemod = 1
			if damagemod > 3:
				damagemod = 3
				
			#Apply critical modifier.
			damage = damage * damagemod
		
		#Check for status effect.
		if statusroll == 1:
			#Change 'message2' to reference the effect.
			statusmessage = "Burn applied! Target takes 2% HP damage per turn for 4 turns."
			
		#Tell bot to post damage.
		await bot.say(message + str(int(damage)) +".\nDeduct 8 SP." +" " + statusmessage)
		message = "Total damage: "
		statusmessage = ""
		
		#Print a confirmation message in the console.
		print("Agilao confirmed. " + str(critroll) + " " + str(statusroll))
		
	if name == "agidyne":
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
			if damagemod < 1:
				damagemod = 1
			if damagemod > 3:
				damagemod = 3
				
			#Apply critical modifier.
			damage = damage * damagemod
		
		#Check for status effect.
		if statusroll == 1:
			#Change 'message2' to reference the effect.
			statusmessage = "Burn applied! Target takes 2% HP damage per turn for 4 turns."
			
		#Tell bot to post damage.
		await bot.say(message + str(int(damage)) +".\nDeduct 12 SP." +" " + statusmessage)
		message = "Total damage: "
		statusmessage = ""
		
		#Print a confirmation message in the console.
		print("Agidyne confirmed. " + str(critroll) + " " + str(statusroll))
		
	if name == "inferno":
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
			if damagemod < 1:
				damagemod = 1
			if damagemod > 3:
				damagemod = 3
				
			#Apply critical modifier.
			damage = damage * damagemod
		
		#Check for status effect.
		if statusroll == 1:
			#Change 'message2' to reference the effect.
			statusmessage = "Burn applied! Target takes 2% HP damage per turn for 4 turns."
			
		#Tell bot to post damage.
		await bot.say(message + str(int(damage)) +".\nDeduct 40 SP." +" " + statusmessage)
		message = "Total damage: "
		statusmessage = ""
		
		#Print a confirmation message in the console.
		print("Inferno confirmed. " + str(critroll) + " " + str(statusroll))
		
	if name == "garu":
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
			if damagemod < 1:
				damagemod = 1
			if damagemod > 3:
				damagemod = 3
				
			#Apply critical modifier.
			damage = damage * damagemod
		
		#Check for status effect.
		if statusroll == 1:
			#Change 'message2' to reference the effect.
			statusmessage = "Dizzy applied! Target deals only 60% damage per turn for 2 turns."
			
		#Tell bot to post damage.
		await bot.say(message + str(int(damage)) +".\nDeduct 4 SP." +" " + statusmessage)
		message = "Total damage: "
		statusmessage = ""
		
		#Print a confirmation message in the console.
		print("Garu confirmed. " + str(critroll) + " " + str(statusroll))
		
	if name == "garula":
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
			if damagemod < 1:
				damagemod = 1
			if damagemod > 3:
				damagemod = 3
				
			#Apply critical modifier.
			damage = damage * damagemod
		
		#Check for status effect.
		if statusroll == 1:
			#Change 'message2' to reference the effect.
			statusmessage = "Dizzy applied! Target deals only 60% damage per turn for 2 turns."
			
		#Tell bot to post damage.
		await bot.say(message + str(int(damage)) +".\nDeduct 8 SP." +" " + statusmessage)
		message = "Total damage: "
		statusmessage = ""
		
		#Print a confirmation message in the console.
		print("Garula confirmed. " + str(critroll) + " " + str(statusroll))
		
	if name == "garudyne":
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
			if damagemod < 1:
				damagemod = 1
			if damagemod > 3:
				damagemod = 3
				
			#Apply critical modifier.
			damage = damage * damagemod
		
		#Check for status effect.
		if statusroll == 1:
			#Change 'message2' to reference the effect.
			statusmessage = "Dizzy applied! Target deals only 60% damage per turn for 2 turns."
			
		#Tell bot to post damage.
		await bot.say(message + str(int(damage)) +".\nDeduct 12 SP." +" " + statusmessage)
		message = "Total damage: "
		statusmessage = ""
		
		#Print a confirmation message in the console.
		print("Garudyne confirmed. " + str(critroll) + " " + str(statusroll))
		
	if name == "pantarhei":
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
			if damagemod < 1:
				damagemod = 1
			if damagemod > 3:
				damagemod = 3
				
			#Apply critical modifier.
			damage = damage * damagemod
		
		#Check for status effect.
		if statusroll == 1:
			#Change 'message2' to reference the effect.
			statusmessage = "Dizzy applied! Target deals only 60% damage per turn for 2 turns."
			
		#Tell bot to post damage.
		await bot.say(message + str(int(damage)) +".\nDeduct 40 SP." +" " + statusmessage)
		message = "Total damage: "
		statusmessage = ""
		
		#Print a confirmation message in the console.
		print("Panta Rhei confirmed. " + str(critroll) + " " + str(statusroll))
		
	if name == "zio":
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
			if damagemod < 1:
				damagemod = 1
			if damagemod > 3:
				damagemod = 3
				
			#Apply critical modifier.
			damage = damage * damagemod
		
		#Check for status effect.
		if statusroll == 1:
			#Change 'message2' to reference the effect.
			statusmessage = "Shock applied! Target can not move for 3 turns, but all who touch the target suffer while Shocked take 100 HP damage."
			
		#Tell bot to post damage.
		await bot.say(message + str(int(damage)) +".\nDeduct 4 SP." +" " + statusmessage)
		message = "Total damage: "
		statusmessage = ""
		
		#Print a confirmation message in the console.
		print("Zio confirmed. " + str(critroll) + " " + str(statusroll))
		
	if name == "zionga":
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
			if damagemod < 1:
				damagemod = 1
			if damagemod > 3:
				damagemod = 3
				
			#Apply critical modifier.
			damage = damage * damagemod
		
		#Check for status effect.
		if statusroll == 1:
			#Change 'message2' to reference the effect.
			statusmessage = "Shock applied! Target can not move for 3 turns, but all who touch the target suffer while Shocked take 100 HP damage."
			
		#Tell bot to post damage.
		await bot.say(message + str(int(damage)) +".\nDeduct 8 SP." +" " + statusmessage)
		message = "Total damage: "
		statusmessage = ""
		
		#Print a confirmation message in the console.
		print("Zionga confirmed. " + str(critroll) + " " + str(statusroll))
		
	if name == "ziodyne":
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
			if damagemod < 1:
				damagemod = 1
			if damagemod > 3:
				damagemod = 3
				
			#Apply critical modifier.
			damage = damage * damagemod
		
		#Check for status effect.
		if statusroll == 1:
			#Change 'message2' to reference the effect.
			statusmessage = "Shock applied! Target can not move for 3 turns, but all who touch the target suffer while Shocked take 100 HP damage."
			
		#Tell bot to post damage.
		await bot.say(message + str(int(damage)) +".\nDeduct 12 SP." +" " + statusmessage)
		message = "Total damage: "
		statusmessage = ""
		
		#Print a confirmation message in the console.
		print("Ziodyne confirmed. " + str(critroll) + " " + str(statusroll))
		
	if name == "thunderreign":
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
			if damagemod < 1:
				damagemod = 1
			if damagemod > 3:
				damagemod = 3
				
			#Apply critical modifier.
			damage = damage * damagemod
		
		#Check for status effect.
		if statusroll == 1:
			#Change 'message2' to reference the effect.
			statusmessage = "Shock applied! Target can not move for 3 turns, but all who touch the target suffer while Shocked take 100 HP damage."
			
		#Tell bot to post damage.
		await bot.say(message + str(int(damage)) +".\nDeduct 40 SP." +" " + statusmessage)
		message = "Total damage: "
		statusmessage = ""
		
		#Print a confirmation message in the console.
		print("Thunder Reign confirmed. " + str(critroll) + " " + str(statusroll))
		
	if name == "bufu":
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
			if damagemod < 1:
				damagemod = 1
			if damagemod > 3:
				damagemod = 3
				
			#Apply critical modifier.
			damage = damage * damagemod
		
		#Check for status effect.
		if statusroll == 1:
			#Change 'message2' to reference the effect.
			statusmessage = "Freeze applied! Target can not move during its next turn."
			
		#Tell bot to post damage.
		await bot.say(message + str(int(damage)) +".\nDeduct 4 SP." +" " + statusmessage)
		message = "Total damage: "
		statusmessage = ""
		
		#Print a confirmation message in the console.
		print("Bufu confirmed. " + str(critroll) + " " + str(statusroll))
		
	if name == "bufula":
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
			if damagemod < 1:
				damagemod = 1
			if damagemod > 3:
				damagemod = 3
				
			#Apply critical modifier.
			damage = damage * damagemod
		
		#Check for status effect.
		if statusroll == 1:
			#Change 'message2' to reference the effect.
			statusmessage = "Freeze applied! Target can not move during its next turn."
			
		#Tell bot to post damage.
		await bot.say(message + str(int(damage)) +".\nDeduct 8 SP." +" " + statusmessage)
		message = "Total damage: "
		statusmessage = ""
		
		#Print a confirmation message in the console.
		print("Bufula confirmed. " + str(critroll) + " " + str(statusroll))
		
	if name == "bufudyne":
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
			if damagemod < 1:
				damagemod = 1
			if damagemod > 3:
				damagemod = 3
				
			#Apply critical modifier.
			damage = damage * damagemod
		
		#Check for status effect.
		if statusroll == 1:
			#Change 'message2' to reference the effect.
			statusmessage = "Freeze applied! Target can not move during its next turn."
			
		#Tell bot to post damage.
		await bot.say(message + str(int(damage)) +".\nDeduct 12 SP." +" " + statusmessage)
		message = "Total damage: "
		statusmessage = ""
		
		#Print a confirmation message in the console.
		print("Bufudyne confirmed. " + str(critroll) + " " + str(statusroll))
		
	if name == "diamonddust":
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
			if damagemod < 1:
				damagemod = 1
			if damagemod > 3:
				damagemod = 3
				
			#Apply critical modifier.
			damage = damage * damagemod
		
		#Check for status effect.
		if statusroll == 1:
			#Change 'message2' to reference the effect.
			statusmessage = "Freeze applied! Target can not move during its next turn."
			
		#Tell bot to post damage.
		await bot.say(message + str(int(damage)) +".\nDeduct 40 SP." +" " + statusmessage)
		message = "Total damage: "
		statusmessage = ""
		
		#Print a confirmation message in the console.
		print("Diamond Dust confirmed. " + str(critroll) + " " + str(statusroll))
		
@bot.command(name="heal")

#Skill List

#Dia
#Diarama
#Diarahan

async def _heal(name, maxhp):
#I got too lazy to comment for a bit.
	name = str(name)
	maxhp = int(maxhp)
	if name == "dia":
		bonus = (maxhp / 4)
		hpgiven = bonus + 75
		hpgiven = int(hpgiven)
		if hpgiven > maxhp:
			hpgiven = maxhp
		await bot.say("Restored " + str(hpgiven) + " HP!")
		print("Dia confirmed.")
		
	if name == "diarama":
		bonus = (maxhp / 2)
		hpgiven = bonus + 150
		hpgiven = int(hpgiven)
		if hpgiven > maxhp:
			hpgiven = maxhp
		await bot.say("Restored " + str(hpgiven) + " HP!")
		print("Diarama confirmed.")
		
	if name == "diarahan":
		await bot.say("Restored " + str(maxhp) + " HP!")
		print("Diarahan confirmed.")

bot.run('-snip-')
