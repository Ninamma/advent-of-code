require 'day_one.rb'

describe DayOne do
    it "can calculate the fuel required for a module" do
        mass_and_fuel = {
            12 => 2,
            14 => 2,
            1969 => 654,
            100756 => 33583
        }

        mass_and_fuel.each do |mass, fuel|
            expect(fuel).to eq(DayOne.calculate(mass))
        end
    end

    it "can read a file of masses and return an array of them" do
        masses = DayOne.get_masses('day_one_test.txt')
        expect(masses).to eq(["12","12","12"])
    end

    it "can calculate the total fuel needed" do
        masses = DayOne.get_masses('day_one_test.txt')
        fuel = DayOne.calculate_total_fuel(masses)
        expect(fuel).to eq(6)
    end

    it "will solve day one part one" do
        masses = DayOne.get_masses('day_one.txt')
        fuel = DayOne.calculate_total_fuel(masses)
        puts fuel
    end
end