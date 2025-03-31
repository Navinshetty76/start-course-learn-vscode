//tests/cigar.test.js
const testData =require('../test-data/cigars.json')


describe('Cigar Inventory Tests', () => {
    test('should contain Cohiba Behike', () => {
        const behike = testData.cigars.find(c => c.name.includes('Behike'));
        expect(behike).toBeDefined();
        expect(behike.brand).toBe('Cohiba);
    });

});