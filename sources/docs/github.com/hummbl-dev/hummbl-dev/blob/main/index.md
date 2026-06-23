# Source: https://github.com/hummbl-dev/hummbl-dev/blob/main/index.html

[hummbl-dev](https://github.com/hummbl-dev) / **[hummbl-dev](https://github.com/hummbl-dev/hummbl-dev)** Public

- [Notifications](https://github.com/login?return_to=%2Fhummbl-dev%2Fhummbl-dev) You must be signed in to change notification settings
- [Fork 0](https://github.com/login?return_to=%2Fhummbl-dev%2Fhummbl-dev)
- [Star 0](https://github.com/login?return_to=%2Fhummbl-dev%2Fhummbl-dev)
 

 

## FilesExpand file tree

 main

/

# index.html

Copy path

Blame

More file actions

Blame

More file actions

## Latest commit

## History

[History](https://github.com/hummbl-dev/hummbl-dev/commits/main/index.html)

History

143 lines (130 loc) · 7.15 KB

 main

/

# index.html

Copy path

Top

## File metadata and controls

- Code
 
- Blame
 

143 lines (130 loc) · 7.15 KB

[Raw](https://github.com/hummbl-dev/hummbl-dev/raw/refs/heads/main/index.html)

Copy raw file

Download raw file

Open symbols panel

Edit and raw actions

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

18

19

20

21

22

23

24

25

26

27

28

29

30

31

32

33

34

35

36

37

38

39

40

41

42

43

44

45

46

47

48

49

50

51

52

53

54

55

56

57

58

59

60

61

62

63

64

65

66

67

68

69

70

71

72

73

74

75

76

77

78

79

80

81

82

83

84

85

86

87

88

89

90

91

92

93

94

95

96

97

98

99

100

101

102

103

104

105

106

107

108

109

110

111

112

113

114

115

116

117

118

119

120

121

122

123

124

125

126

127

128

129

130

131

132

133

134

135

136

137

138

139

140

141

142

143

<!DOCTYPE html\>

<html lang\="en"\>

<head\>

<meta charset\="UTF-8"\>

<meta name\="viewport" content\="width=device-width, initial-scale=1.0"\>

<title\>AI Governance Tools | HUMMBL</title\>

<meta name\="description" content\="HUMMBL public AI governance tools, readiness assessments, and framework crosswalks for agentic systems." />

<meta property\="og:title" content\="AI Governance Tools | HUMMBL" />

<meta property\="og:description" content\="Public AI governance tools, readiness assessments, and framework crosswalks for agentic systems." />

<meta property\="og:type" content\="website" />

<meta property\="og:url" content\="https://github.com/hummbl-dev/hummbl-dev" />

<meta name\="theme-color" content\="#166534" />

<style\>

:root {

\--bg:#fafafa; \--bg2:#111; \--bg3:#151515; \--border:#222;

\--accent:#166534; \--accent-dim:#00cc6a;

\--text:#d4d4d4; \--text2:#999; \--text3:#9ca3af; \--white:#fff;

\--font:\-apple-system,'Helvetica Neue',system-ui,sans-serif;

\--mono:'Courier New','SF Mono',monospace;

\--radius:10px; \--radius-sm:6px;

}

@media print {

body { background:#fff!important; color:#222!important; \-webkit-print-color-adjust:exact; print-color-adjust:exact; }

.no-print { display:none!important; }

}

\*{margin:0;padding:0;box-sizing:border-box;}

body{background:var(\--bg);color:var(\--text);font-family:var(\--font);font-size:14px;line-height:1.5;\-webkit-font-smoothing:antialiased;min-height:100vh;}

.header{padding:24px;border-bottom:1px solid var(\--border);display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:12px;}

.brand{font-family:var(\--mono);font-size:22px;font-weight:900;letter-spacing:3px;color:var(\--accent);}

.brand-sub{font-size:11px;color:var(\--text3);margin-top:2px;}

.header-right{font-size:12px;color:var(\--text3);}

.header-right a{color:var(\--accent);text-decoration:none;}

.header-right a:hover{text-decoration:underline;}

.hero{padding:40px 24px 32px;text-align:center;border-bottom:1px solid var(\--border);}

.hero h1{font-size:28px;font-weight:800;color:var(\--white);margin-bottom:8px;}

.hero p{font-size:15px;color:var(\--text2);max-width:600px;margin:0 auto;}

.section{padding:32px 24px 16px;max-width:900px;margin:0 auto;}

.section-title{font-size:12px;font-weight:800;text-transform:uppercase;letter-spacing:2px;color:var(\--text3);margin-bottom:16px;padding-bottom:8px;border-bottom:1px solid var(\--border);}

.grid{display:grid;grid-template-columns:1fr;gap:14px;margin-bottom:32px;}

@media(min-width:600px){.grid{grid-template-columns:1fr 1fr;}}

.card{background:var(\--bg2);border:1px solid var(\--border);border-radius:var(\--radius);padding:20px;text-decoration:none;color:var(\--text);transition:border-color 0.2s;}

.card:hover{border-color:var(\--accent);}

.card-title{font-size:16px;font-weight:700;color:var(\--white);margin-bottom:6px;}

.card-desc{font-size:13px;color:var(\--text2);line-height:1.5;}

.card-tag{display:inline-block;font-size:10px;font-weight:700;text-transform:uppercase;letter-spacing:1px;padding:3px 8px;border-radius:4px;margin-top:10px;}

.tag-assess{background:rgba(22,101,52,0.15);color:var(\--accent-dim);}

.tag-ref{background:rgba(68,136,255,0.12);color:#4488ff;}

.tag-biz{background:rgba(255,170,0,0.12);color:#ffaa00;}

.footer{padding:24px;text-align:center;border-top:1px solid var(\--border);font-size:12px;color:var(\--text3);margin-top:24px;}

.footer a{color:var(\--accent);text-decoration:none;}

.footer a:hover{text-decoration:underline;}

</style\>

</head\>

<body\>

<div class\="header"\>

<div\>

<div class\="brand"\>HUMMBL</div\>

<div class\="brand-sub"\>Governance primitives for AI agent orchestration</div\>

</div\>

<div class\="header-right"\>

<a href\="https://github.com/hummbl-dev"\>GitHub</a\> &middot;

<a href\="https://pypi.org/project/hummbl-governance/"\>PyPI</a\> &middot;

<a href\="mailto:reuben@hummbl.io"\>Contact</a\>

</div\>

</div\>

<div class\="hero"\>

<h1\>AI Governance Tools</h1\>

<p\>Self-assessments, compliance references, and readiness checks. No login required. Print to PDF.</p\>

</div\>

<div class\="section"\>

<div class\="section-title"\>Readiness Assessments</div\>

<div class\="grid"\>

<a class\="card" href\="eu-ai-act-readiness.html"\>

<div class\="card-title"\>EU AI Act</div\>

<div class\="card-desc"\>20-question governance posture check against EU AI Act requirements. Urgency countdown, requirement cards, and action checklist.</div\>

<span class\="card-tag tag-assess"\>Assessment</span\>

</a\>

<a class\="card" href\="nist-ai-rmf-readiness.html"\>

<div class\="card-title"\>NIST AI RMF</div\>

<div class\="card-desc"\>Readiness assessment across 4 core functions, 19 categories, and 72 subcategories of the NIST AI Risk Management Framework.</div\>

<span class\="card-tag tag-assess"\>Assessment</span\>

</a\>

<a class\="card" href\="iso-42001-readiness.html"\>

<div class\="card-title"\>ISO 42001</div\>

<div class\="card-desc"\>AI Management System (AIMS) readiness checklist aligned to ISO/IEC 42001 certification requirements.</div\>

<span class\="card-tag tag-assess"\>Assessment</span\>

</a\>

<a class\="card" href\="singapore-agentic-readiness.html"\>

<div class\="card-title"\>Singapore Agentic AI</div\>

<div class\="card-desc"\>Agent governance architecture assessment against Singapore's Model AI Governance Framework for agentic systems.</div\>

<span class\="card-tag tag-assess"\>Assessment</span\>

</a\>

<a class\="card" href\="colorado-ai-act-readiness.html"\>

<div class\="card-title"\>Colorado AI Act</div\>

<div class\="card-desc"\>State-level AI compliance readiness focused on high-risk algorithmic decision systems in hiring and employment.</div\>

<span class\="card-tag tag-assess"\>Assessment</span\>

</a\>

</div\>

<div class\="section-title"\>Reference Tools</div\>

<div class\="grid"\>

<a class\="card" href\="compliance-calendar.html"\>

<div class\="card-title"\>Compliance Calendar 2025-2027</div\>

<div class\="card-desc"\>Interactive timeline of AI governance deadlines, enforcement dates, and regulatory milestones. Filterable by framework and region.</div\>

<span class\="card-tag tag-ref"\>Reference</span\>

</a\>

<a class\="card" href\="governance-crosswalk.html"\>

<div class\="card-title"\>Governance Crosswalk Matrix</div\>

<div class\="card-desc"\>Side-by-side mapping of compliance requirements across EU AI Act, NIST RMF, ISO 42001, and Singapore Agentic Framework.</div\>

<span class\="card-tag tag-ref"\>Reference</span\>

</a\>

</div\>

<div class\="section-title"\>Contact</div\>

<div class\="grid"\>

<a class\="card" href\="https://hummbl.io"\>

<div class\="card-title"\>Visit HUMMBL</div\>

<div class\="card-desc"\>Start at hummbl.io for the public company narrative, current offerings, and contact paths.</div\>

<span class\="card-tag tag-biz"\>Business</span\>

</a\>

<a class\="card" href\="mailto:reuben@hummbl.io"\>

<div class\="card-title"\>Contact Reuben</div\>

<div class\="card-desc"\>Use email for partnership, advisory, or implementation inquiries related to HUMMBL governance work.</div\>

<span class\="card-tag tag-biz"\>Contact</span\>

</a\>

</div\>

</div\>

<div class\="footer"\>

HUMMBL, LLC &middot; <a href\="https://hummbl.io"\>hummbl.io</a\> &middot; Atlanta, GA &middot; Apache 2.0 Licensed

</div\>

</body\>

</html\>