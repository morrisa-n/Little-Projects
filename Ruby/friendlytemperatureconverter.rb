puts "Hello, I am your friendly temperature converter, here to
change temperatures from Fahrenheit to Celsius for you,
or vice versa."

puts "Which would you like to convert from, Fahrenheit or Celsius?\n(Enter full name or first letter)"

type1 = gets.chomp.downcase

if type1 == "fahrenheit" || type1 == "f"
    puts "Okay. And what is the temperature you'd like to convert to Celsius? (Numbers only, please)"
    temperature = gets.to_i
    final = (temperature - 32) * 5 / 9
    puts "#{temperature} degrees Fahrenheit is #{final} degrees Celsius."
else
    puts "Okay. And what is the temperature you'd like to convert to Fahrenheit? (Numbers only, please)"
    temperature = gets.to_i
    final = (temperature * (9 / 5)) + 32
    puts "#{temperature} degrees Celsius is #{final} degrees Fahrenheit"
end
puts "Have a wonderful day. :)"
