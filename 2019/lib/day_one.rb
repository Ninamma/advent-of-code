class DayOne
    def self.calculate(mass)
         mass/3.floor - 2
    end

    def self.get_masses(filename)
        current_dir = File.dirname(__FILE__)
        input_file_path = File.join(current_dir, '../inputs', filename)
        file = File.open(input_file_path)
        file.readlines.map(&:chomp)
    end

    def self.calculate_total_fuel(mass_array)
        sum = 0
        mass_array.each do |mass|
            mass = mass.to_i
            sum += DayOne.calculate(mass)
        end
        sum
    end
end