CREATE TABLE `instructor` (
 `instructor_id` int(11) NOT NULL,
 `name` varchar(50) NOT NULL,
 `department` varchar(200) NOT NULL,
 `rating` int(11) DEFAULT 0,
 `school` varchar(200) DEFAULT NULL,
 PRIMARY KEY (`instructor_id`)
)

CREATE TABLE `minor` (
 `id` int(11) NOT NULL,
 `name` varchar(100) NOT NULL,
 `school` varchar(200) NOT NULL,
 `req_ch` int(11) NOT NULL,
 PRIMARY KEY (`id`)
) 

CREATE TABLE `Major` (
 `id` int(11) NOT NULL,
 `name` varchar(30) NOT NULL,
 `school` varchar(30) NOT NULL,
 `req_ch` int(11) NOT NULL,
 PRIMARY KEY (`id`)
)

CREATE TABLE `courses` (
 `course_id` int(11) NOT NULL,
 `name` varchar(200) NOT NULL,
 `school` varchar(200) NOT NULL,
 `major` int(11) DEFAULT NULL,
 `instructor` int(11) DEFAULT NULL,
 `course_cap` int(11) DEFAULT NULL CHECK (`course_cap` > 0),
 `semester` varchar(100) DEFAULT NULL CHECK (lcase(`semester`) in ('fall','spring','summer')),
 `year` int(11) NOT NULL CHECK (`year` > 2000),
 `credit_hours` int(11) NOT NULL,
 PRIMARY KEY (`course_id`),
 FOREIGN KEY (`major`) REFERENCES `Major` (`id`),
 FOREIGN KEY (`instructor`) REFERENCES `instructor` (`instructor_id`) ON DELETE SET NULL
)

CREATE TABLE `minor_courses` (
 `id` int(11) NOT NULL AUTO_INCREMENT,
 `minor` int(11) NOT NULL,
 `course_id` int(11) DEFAULT NULL,
 PRIMARY KEY (`id`),
 FOREIGN KEY (`minor`) REFERENCES `minor` (`id`) ON DELETE CASCADE,
 FOREIGN KEY (`course_id`) REFERENCES `courses` (`course_id`) ON DELETE SET NULL
) 

CREATE TABLE `prereqs` (
 `course_id` int(11) NOT NULL,
 `prereq_id` int(11) NOT NULL,
 PRIMARY KEY (`course_id`,`prereq_id`),
 FOREIGN KEY (`course_id`) REFERENCES `courses` (`course_id`) ON DELETE CASCADE,
 FOREIGN KEY (`prereq_id`) REFERENCES `courses` (`course_id`) ON DELETE CASCADE
) 

CREATE TABLE `students` (
 `roll_number` int(11) NOT NULL,
 `full_name` varchar(50) NOT NULL,
 `grad_year` int(11) NOT NULL,
 `cgpa` float DEFAULT 0,
 `ch_taken` int(11) DEFAULT 0,
 `major` int(11) DEFAULT NULL,
 PRIMARY KEY (`roll_number`),
 FOREIGN KEY (`major`) REFERENCES `Major` (`id`)
) 

CREATE TABLE `student_course_info` (
 `roll_number` int(11) NOT NULL,
 `course_id` int(11) NOT NULL,
 `course_gpa` float DEFAULT NULL CHECK (`course_gpa` >= 0 and `course_gpa` <= 4),
 `semester` varchar(50) NOT NULL CHECK (lcase(`semester`) in ('fall','spring','summer')),
 `year` int(11) NOT NULL,
 PRIMARY KEY (`roll_number`,`course_id`),
 FOREIGN KEY (`roll_number`) REFERENCES `students` (`roll_number`) ON DELETE CASCADE,
 FOREIGN KEY (`course_id`) REFERENCES `courses` (`course_id`) ON DELETE CASCADE
) 

CREATE TABLE `advisor` (
 `roll_number` int(11) NOT NULL,
 `instructor_id` int(11) DEFAULT NULL,
 PRIMARY KEY (`roll_number`),
 FOREIGN KEY (`roll_number`) REFERENCES `students` (`roll_number`) ON DELETE CASCADE,
 FOREIGN KEY (`instructor_id`) REFERENCES `instructor` (`instructor_id`) ON DELETE SET NULL
)

CREATE TABLE `antireqs` (
 `course_id` int(11) NOT NULL,
 `antireq_id` int(11) NOT NULL,
 PRIMARY KEY (`course_id`,`antireq_id`),
 FOREIGN KEY (`course_id`) REFERENCES `courses` (`course_id`) ON DELETE CASCADE,
 FOREIGN KEY (`antireq_id`) REFERENCES `courses` (`course_id`) ON DELETE CASCADE
) 

CREATE TABLE `major_cores` (
 `id` int(11) NOT NULL AUTO_INCREMENT,
 `course_id` int(11) NOT NULL,
 `name` varchar(200) NOT NULL,
 `major` int(11) NOT NULL,
 PRIMARY KEY (`id`),
 FOREIGN KEY (`course_id`) REFERENCES `courses` (`course_id`) ON DELETE CASCADE,
 FOREIGN KEY (`major`) REFERENCES `Major` (`id`) ON DELETE CASCADE
)
