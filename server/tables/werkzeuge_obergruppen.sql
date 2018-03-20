-- phpMyAdmin SQL Dump
-- version 3.3.2deb1ubuntu1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Erstellungszeit: 17. Dezember 2012 um 14:22
-- Server Version: 5.1.66
-- PHP-Version: 5.3.2-1ubuntu4.18

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Datenbank: `vamos`
--

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `werkzeuge_obergruppen`
--

CREATE TABLE IF NOT EXISTS `werkzeuge_obergruppen` (
  `id` int(11) NOT NULL,
  `bezeichnung` text CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Daten für Tabelle `werkzeuge_obergruppen`
--

INSERT INTO `werkzeuge_obergruppen` (`id`, `bezeichnung`) VALUES
(1, 'Pfanne'),
(2, 'Topf'),
(3, 'Herd'),
(4, 'Backpapier'),
(5, 'Form'),
(6, 'Kühlschrank'),
(7, 'Umluftherd'),
(8, 'Sieb'),
(9, 'Blech'),
(10, 'Geschirr'),
(11, 'Wok'),
(12, 'Alufolie'),
(13, 'Mixer'),
(14, 'Schneebesen'),
(15, 'Folie'),
(16, 'Schmortopf'),
(17, 'Tortenring'),
(18, 'Waffeleisen'),
(19, 'Tuch'),
(20, 'Spritzbeutel'),
(21, 'Küchenmaschine'),
(22, 'Küchenpapier'),
(23, 'Rührgerät'),
(24, 'Grill'),
(25, 'Schüssel'),
(26, 'Pürierstab'),
(27, 'Kuchengitter'),
(28, 'Mikrowelle'),
(29, 'Beutel'),
(30, 'Tortenplatte'),
(31, 'Gitter'),
(32, 'Nudelholz'),
(33, 'Arbeitsplatte'),
(34, 'Schaumlöffel'),
(35, 'Presse'),
(36, 'Spieße'),
(37, 'Kochlöffel'),
(38, 'Schnellkochtopf'),
(39, 'Schöpfkelle'),
(40, 'Küchengarn'),
(41, 'Tülle'),
(42, 'Fleischwolf'),
(43, 'Sparschäler'),
(44, 'Muffinform'),
(45, 'Pinsel'),
(46, 'Römertopf'),
(47, 'Schere'),
(48, 'Backrahmen'),
(49, 'Ausstecher'),
(50, 'Eismaschine'),
(51, 'Tablett'),
(52, 'Nudelmaschine'),
(53, 'Grillpfanne'),
(54, 'Becher'),
(55, 'Einmachglas'),
(56, 'Dessertschalen'),
(57, 'Portionsteller'),
(58, 'Toaster'),
(59, 'Kartoffelstampfer'),
(60, 'Cocktailglas'),
(61, 'Küchenreibe'),
(62, 'Kugelausstecher'),
(63, 'Zestenreißer'),
(64, 'Salatschleuder'),
(65, 'Kaffeemühle'),
(66, 'Wasserkocher'),
(67, 'Friteuse');
