<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
     "http://www.w3.org/TR/html4/transitional.dtd">
<html>
<head>

  <meta http-equiv="content-type" content="text/html; charset=utf-8"/>
  <title>PowerPoint 演示文稿</title>
  <meta name="generator" content="LibreOffice 7.4.7.2 (Linux)"/>
  <meta name="author" content="gaohanghang"/>
  <meta name="created" content="2024-05-08T08:34:26"/>
  <meta name="changedby" content="Toyo Ntewo"/>
  <meta name="changed" content="2024-05-08T08:34:26"/>
  <meta name="AppVersion" content="14.0000"/>
  <meta name="KSOProductBuildVer" content="1033-5.6.0.8082"/>
  <meta name="PresentationFormat" content="宽屏"/>
  <meta name="Slides" content="14"/>
</head>
<body>
<h1></h1>
<p><b>DEPLOYMENT OF A HONEYPOT SYSTEM FOR </b></p>
<p><b>CYBER-ATTACK DETECTION</b></p>
<p><b></b></p>
<p><b>BY</b></p>
<p><b></b></p>
<p><b>NTEWO TOYO </b></p>
<p><b>20/SCI01/081</b></p>
<p><b></b></p>
<p><b>ALOBA SUAD</b></p>
<p><b>21/SCI01/075</b></p>
<p><b></b></p>
<p><b>SUPERVISOR:</b></p>
<p><b>Mr. FEMI SANYA</b></p>
<p><b></b></p>
<p><b>MAY, 2023</b></p>
<h1 style="page-break-before:always; "></h1>
<p><b>01 Background of Study			07 Conclusion	</b></p>
<p><b>02 Problem Statement</b></p>
<p><b>03 Aim and Objective</b></p>
<p><b>04 Literature review</b></p>
<p><b>05 System analysis</b></p>
<p><b>06 Results</b></p>
<p><b>Outline</b></p>
<h1 style="page-break-before:always; "></h1>
<p><b>01</b></p>
<p><b>Background</b></p>
<p>The concept of honeypots has a rich history dating back decades and has gained significant attention in recent years. Originally articulated by Spitzner in 2002 as a security resource intentionally probed or attacked, honeypots, Honeypots can also be described as virtual decoys strategically placed to mimic real systems.</p>
<p> </p>
<h1 style="page-break-before:always; "></h1>
<p><b>02</b></p>
<p><b>Problem Statement</b></p>
<p>Traditional security measures like Intrusion Detection Systems (IDS) and firewalls aim to detect abnormal activities, but they often struggle with high false alarm rates and lack sufficient detail in generated alerts for effective analysis. This limitation means that security teams may spend valuable time investigating false positives, diverting attention from genuine threats. </p>
<h1 style="page-break-before:always; "></h1>
<p><b>03</b></p>
<p><b>Aim &amp; Objectives</b></p>
<p> </p>
<p>This project Aims to design and implement a honeypot system for cyber-attack detection.</p>
<p>Objectives:</p>
<p>1. To Implement a honeypot system in a controlled environment (cloud server).</p>
<p>2. To analyse the data on attacker activities and footprints stored in the log.</p>
<p>3. Give valuable insights into the behaviors and methodologies of attackers from 	the analyzed log in (2) to enable more effective and efficient response.</p>
<p><b></b></p>
<h1 style="page-break-before:always; "></h1>
<p><b>03</b></p>
<p><b>Methodology</b></p>
<p>Our methodology entails a systematic approach across three key stages.</p>
<p>Firstly, </p>
<p><b>In Cloud Platform selection:</b></p>
<p>A comprehensive evaluation based on scalability, availability, performance, and compliance. This involves accessing factors like data center locations, network traffic and adherence to data sovereignty regulations, alongside evaluating support for virtual machines, containers, and networking capabilities. </p>
<p>After the platform selection, we proceed with the <b>Installation and Configuration</b> of honeypot software on cloud-hosted VMs or containers, tailoring configurations to simulate diverse services and protocols while implementing stringent security measures.</p>
<h1 style="page-break-before:always; "></h1>
<p><b>04</b></p>
<p><b>Literature Review</b></p>
<p> </p>
<table>
  <tr>
    <td>
<p><b>Paper</b></p>
    </td>
    <td>
<p><b>Method Detail </b></p>
    </td>
    <td>
<p><b>Mitigated attacks</b></p>
    </td>
    <td>
<p><b>Vulnerabilities/Limitations</b></p>
    </td>
  </tr>
  <tr>
    <td>
<p><b>(Kapczynski and Lawnik, 2019) </b></p>
    </td>
    <td>
<p>Using cyphers with adjusting key lengths</p>
    </td>
    <td>
<p>This system is built to withstand a variety of assaults, including plaintext, related-key, and side-channel attacks.</p>
    </td>
    <td>
<p>Execution space and time are greatly expanded.</p>
    </td>
  </tr>
  <tr>
    <td>
<p><b>(Aggarwal and Maurer, 2016)</b></p>
    </td>
    <td>
<p>Utilising the generic ring method for RSA factoring</p>
    </td>
    <td>
<p>RSA's reduction of factoring problems</p>
    </td>
    <td>
<p>Various attacks involving cryptoanalysis are feasible.</p>
    </td>
  </tr>
  <tr>
    <td>
<p><b>(Hwang et al, 2016) </b></p>
    </td>
    <td>
<p>Certificates are encrypted with pairless cryptography.</p>
    </td>
    <td>
<p>Defends against assaults by employing specific cypher messages</p>
    </td>
    <td>
<p>The design is vulnerable to Denial-of-Service assaults since it depends so heavily on bandwidth.</p>
    </td>
  </tr>
</table>
<h1 style="page-break-before:always; "></h1>
<p><b>05</b></p>
<p><b>System Analysis</b></p>
<h1 style="page-break-before:always; "></h1>
<p>According to the system log data, the United States accounted for the highest proportion of attempted system accesses, comprising 57.98%. Following closely behind, France constituted 20.22%, with China contributing 14.62%. It's noteworthy that a significant portion of these access attempts originated from Asia and Europe, indicating a widespread presence of potential attackers across these regions</p>
<h1 style="page-break-before:always; "></h1>
<p>In the log data, specific IP addresses stand out for their persistent attempts to intrude. Notably, IP address 154.27.68.195 recorded the highest number of attempts, totaling 441. Following closely behind is 138.68.224.69, which made 222 attempts, trailed by 51.15.17.105 with 212 attempts, and 219.134.218.250 with 131 attempts. These repeated intrusion attempts from these IPs raiseconcerns about potential security vulnerabilities and the need for enhanced protective measures.</p>
<h1 style="page-break-before:always; "></h1>
<p><b>06</b></p>
<p><b>Data Analysis result summary</b></p>
<table>
  <tr>
    <td>
<p><b>CATEGORY</b></p>
    </td>
    <td>
<p><b>DESCRIPTION</b></p>
    </td>
    <td>
<p><b>RESULT</b></p>
    </td>
  </tr>
  <tr>
    <td>
<p>Basic information</p>
    </td>
    <td>
<p>Shape of the dataset</p>
    </td>
    <td>
<p>1197 * 10</p>
    </td>
  </tr>
  <tr>
    <td>
<p>Basic information</p>
    </td>
    <td>
<p>Column names</p>
    </td>
    <td>
<p>id, ymd, time, session, from_ip_address, to_ip_address, username, password, success, country </p>
    </td>
  </tr>
  <tr>
    <td>
<p>Basic information</p>
    </td>
    <td>
<p>Data types of columns</p>
    </td>
    <td>
<p>Integer &amp; Object</p>
    </td>
  </tr>
  <tr>
    <td>
<p>Summary Statistics</p>
    </td>
    <td>
<p>Number of records </p>
    </td>
    <td>
<p>1197</p>
    </td>
  </tr>
  <tr>
    <td>
<p>Counting Values</p>
    </td>
    <td>
<p>Counts of success values</p>
    </td>
    <td>
<p>Failed: 869, Successful: 328</p>
    </td>
  </tr>
  <tr>
    <td>
<p>Counting Values</p>
    </td>
    <td>
<p>Counts of country values</p>
    </td>
    <td>
<p>United States: 694, France: 242, China: 175, South Korea: 21</p>
    </td>
  </tr>
  <tr>
    <td>
<p>Missing Values</p>
    </td>
    <td>
<p>Missing values in each column</p>
    </td>
    <td>
<p>password: 3</p>
    </td>
  </tr>
  <tr>
    <td>
<p>Successful Logins</p>
    </td>
    <td>
<p>Successful logins by username</p>
    </td>
    <td>
<p>admin: 15, oracle: 28, root: 218, ubuntu: 17</p>
    </td>
  </tr>
</table>
<h1 style="page-break-before:always; "></h1>
<h1 style="page-break-before:always; "></h1>
<p><b>- Akkaya, D., &amp; Thalgott, F. (2010)</b>. Honeypots in network security. </p>
<p><b>- Anicas, M. (2015)</b>. How to install Elasticsearch, logstash, and kibana (ELK Stack) on Ubuntu 14.04. </p>
<p><b>- Dittrich, D. (2004)</b>. Creating and managing distributed honeynets using honeywalls. Draft. University of Washington.</p>
<p><b>- Döring, C. (2005)</b>. Improving network security with honeypots. Darmstadt: University of Applied Sciences.</p>
<p><b>- Hoque, M. S., &amp; Bikas, M. A. (2012)</b>. An implementation of an intrusion detection system using a genetic algorithm. International Journal of Network Security &amp; Its Applications (IJNSA). </p>
<p><b>- Jaiganesh, V., Sumathi, D. P., &amp; A.Vinitha. (2013)</b>. Classification algorithms in intrusion detection system: A survey. A Vinitha et al. Int. J. Computer Technology &amp; Applications. </p>
<p>No Author listed. (https://www.honeyd.org/)</p>
<p><b>- Ralph E.S Jr</b> (No date listed): How to build and use a honeypot.</p>
<p>Deception Toolkit, <u>https://all.net/dtk/index.html</u> fetched 5/02/2015</p>
<p><b>REFERENCES </b></p>
<h1 style="page-break-before:always; "></h1>
<p>T H A N K S</p>
</body>
</html>
