# Logic Audit Example

## Target

- Chapter / outline node: ch001 request planning
- Proposal: 主角提出一项影响地方税粮和军需运输的制度建议。
- Historical period: 明末示例期
- Place: 北京及周边州县
- Related timeline events: @event:event-1644-03-19-li-zicheng-beijing
- Related lore/source ids: @lore:lore-ming-salary-system, @source:source-example-ming-institution

## Verdict

NEEDS_USER_DECISION

## Role findings

### historian_reviewer

- Objections: 示例项目尚未绑定真实项目史料，不能直接入 canon。
- Hidden costs: 若改动税粮制度，后续时间线需记录真实史与架空史差异。
- Likely resistance: 既有官僚体系会要求成例、上谕或地方试行依据。
- Second-order consequences: 可能改变地方军需、民变压力和官员责任链。
- Required repairs: 替换示例来源，补真实史料和具体年月。

### institution_reviewer

- Objections: 需说明谁有权提出、批准、执行和稽核该建议。
- Hidden costs: 文书流程、户部/地方衙门责任、胥吏执行成本。
- Likely resistance: 地方官、胥吏、既得利益者可能拖延或阳奉阴违。
- Second-order consequences: 可能造成账册口径变化和追责风险。
- Required repairs: 写入制度流程和责任主体。

### logistics_reviewer

- Objections: 军需运输不能只写命令，需有路程、车船、人畜和季节限制。
- Hidden costs: 粮耗、损耗、押运、道路/河道状态。
- Likely resistance: 民夫征发和运输摊派会引发逃避。
- Second-order consequences: 若运输改善，战局时间线可能被改写。
- Required repairs: 补路线、天数、损耗估计。

### economics_reviewer

- Objections: 税粮和军需变化会改变激励结构。
- Hidden costs: 征收成本、折色价格、地方摊派。
- Likely resistance: 纳税户、士绅和商人会寻找转嫁方式。
- Second-order consequences: 物价和劳役负担可能影响民心。
- Required repairs: 补财政来源和受损/受益群体。

### military_reviewer

- Objections: 需说明军队是否有训练、纪律和军官能力承接变化。
- Hidden costs: 军需改善不等于战斗力立即提高。
- Likely resistance: 将领可能截留资源或虚报兵额。
- Second-order consequences: 敌方会观察并调整战术。
- Required repairs: 补军中执行链和时间滞后。

### commoner_reviewer

- Objections: 普通百姓首先感受的是摊派、徭役和口粮风险。
- Hidden costs: 家庭劳力被抽走，春耕秋收受影响。
- Likely resistance: 逃役、谣言、隐匿人口或投靠豪强。
- Second-order consequences: 民怨会影响地方稳定。
- Required repairs: 补民间反应和缓冲措施。

### gentry_reviewer

- Objections: 士绅会评估该建议是否损害地方控制力。
- Hidden costs: 需要乡约、宗族、书院和地方网络配合或沉默。
- Likely resistance: 可能通过舆论、诉讼、拖延账册反制。
- Second-order consequences: 主角与地方精英关系会改变。
- Required repairs: 补士绅立场分化。

## Final canon decision

- Decision: NEEDS_USER_DECISION
- Adopted facts: 无；示例仅作格式说明。
- Rejected facts: 不得把本示例当成项目 canon。
- Mandatory repairs before prose: 替换来源、补时间地点、补流程和后果。
- Ledger updates required: `ledgers/` 中记录制度、财政、军需后果。
- Timeline updates required: 如采纳，写入 `timelines/alt-history.md`。
- Lore/source updates required: 补项目自有 source note。
- Work queue updates required: 将审计修复项加入下一章 request。

## Completion status

- logic_audit_required: yes
- logic_audit_status: FAIL
- next stop point: wait for user-owned sources and canon decision.
