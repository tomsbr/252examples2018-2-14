/**
 * The student class encapsulates all
 * of the properties and methods
 * 
 */
function Student(fn, Ln) {
	this.first_name = fn;
	this.last_name = ln;
	this.courses = [];
	this.enroll = (crs) => {
		this.courses.push(crs);
	};
}

module.exports = Student;